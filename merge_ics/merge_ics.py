from ics import Calendar
import glob
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = "Merge ICS files into one ICS file for easy import into Google Calendar.")
    parser.add_argument("input", nargs="*", help = "Input ICS files.")
    parser.add_argument("-o", "--output", default = "merged.ics",
            help = "Output file. Default: merged.ics")
    args = parser.parse_args()
    return(args)

def main():
    args = parse_args()
    # create new calendar and add all events from ics files to it
    new_cal = Calendar()

    if len(args.input) == 0:
        print("No input ICS files specified, using all *.ics files in cwd.")
        ics_files = glob.glob("*.ics")
    else:
        ics_files = args.input

    for ics_file in ics_files:
        with open(ics_file, "r") as f:
            cal = Calendar(f.read())
            for event in cal.events:
                new_cal.events.add(event)

    # then write out the result
    with open(args.output, "w") as f:
        f.writelines(new_cal)


if __name__ == "__main__":
    main()
