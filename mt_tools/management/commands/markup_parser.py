from django.core.management.base import BaseCommand
import pendulum
import pprint

tag_default_date="DEFAULT DATE"
tag_publication="PUBLICATION"
tag_region="REGION"

"""
    This management tool (MT) takes in an article that has been manually marked up and parses and breaks down the logic
    into database tables (database brd_pending). There is no attempt to populate the tables with actual foreign keys -
    that will be done by another MT.
"""

"""
    Markup rules:

    [] indicates a markup block
    Within these braces, the following apply
    l - location, place, e.g. Glasgow
    sl <text> - sublocation of subsequent artefacts (e.g. Erecting Shop Yard)
    [dt d/m/y] - date of subsequent events
    [edt] - end that date and revert to article date.

    A suffix of,[A-Z] means something too. Currently, a suffix S means silent (informational only)

"""

class MarkUpParsing(Exception):
    pass

class InvalidMarkUp(Exception):
    pass

class Command(BaseCommand):
    help = "Read in data from a markup text file and parse it and break down the logic, populating work tables"
    missing_args_message = "You must supply the input filename to be processed"

    region = None
    publication = None
    pen_default_date = None
    line_count = 1

    

    def process_tag(self, tag):
        """
            We have a tag, the first 'bit' of which is an indicator of what the information contained within is
            and any behavioural actions that need to be applied to it. For instance, it may be for information only,
            in which case it doesn't get printed.
        """

        return 

    def add_arguments(self, parser):
        # Mandatory argument
        parser.add_argument(
            "file",
            help="Update database. Default is to reset database.",
            type=str
        )

    def insert_pending_atr(self, line):
        inside_brackets = False  # Flag to track whether currently inside brackets
        current_markup = ""  # Variable to store the current markup

        """
            The input string contains 3 parts: a title, a date and the text. If there is no date supplied, the word 'def' will be used
            and the default date is used.
        """
        title, date, text = line.split('#')

        if date == 'def':
            date = self.pen_default_date
        else:
            d, m, y = date.split('/')
            date = pendulum.datetime(int(y), int(m), int(d))

        title = title.title()

        char_count = 0

        for char in text:
            char_count += 1

            if char == '[':
                try:
                    if inside_brackets:
                        raise MarkUpParsing
                except MarkUpParsing:
                    print()
                    print(f"ERROR: Malformed mark up (near character '[', position {char_count}) on line {self.line_count}")
                    exit(1)
                 
                inside_brackets = True

            elif char == ']':
                try:
                    if not inside_brackets:
                        raise MarkUpParsing
                except MarkUpParsing:
                    print()
                    print(f"ERROR: Malformed mark up (near character ']', position {char_count}) on line {self.line_count}")
                    exit(1)
                
                inside_brackets = False

                # trigger processing of tag
                self.process_tag(current_markup)
                current_markup = ""
            else:
                if inside_brackets:
                    # Collect characters within brackets
                    current_markup += char
                else:
                    # Print characters outside brackets
                    print(char, end='')
            
        print()

        # Process and print any remaining markup outside brackets

    def handle(self, *args, **kwargs):
        debug = False

        inputfile = kwargs['file']
        
        with open(inputfile) as my_file:
            contents = my_file.readlines()

        # 1st line must always hold the source publication details
        _, self.publication = contents[0].strip().split('#')

        for line in contents[1:]:
            self.line_count += 1

            line = line.strip() # remove trailing carriage return

            if len(line) == 0:
                continue

            if line == "STOP":
                print("Breaking...")
                break

            """
                From now on we are dealing with interesting data.
                There are several types that modify subsequent information:
                    DEFAULT DATE: changes the default date from now until the end or if
                    another occurs in the meantime.
                    REGION: the operating region under review

                    Everything else is local information that needs to be parsed using the rules outlined in the 
                    comments at the top of this file.
            """

            if line[:len(tag_default_date)] == tag_default_date:
                _, default_date = line.split('#')

                d, m, y = default_date.split('/')
                self.pen_default_date = pendulum.datetime(int(y), int(m), int(d))
                print(self.pen_default_date)
                continue

            if line[:len(tag_region)] == tag_region:
                _, region = line.split('#')
                print(region)
                continue

            # Everything beyond this point is a new line of information
            self.insert_pending_atr(line)

        print(f"Finished processing {self.line_count} lines")

        