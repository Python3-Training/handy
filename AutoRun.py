#!/usr/bin/enc python3
'''Mission: Monitor and run a Python script whenever it changes.
Show errors, output, and execution time whenever the hosted script is run.

CAVEATS: GREAT DESTRUCTIVE POTENTIAL HERE - SCRIPT WILL RUN
         YOU ARE RESPONSIBLE - BE SURE NO HARM.

File: AutoRun.py
Status: Lightly tested.
Version: 0.1

'''
import os
import time
import subprocess
import sys
import argparse


def run_script(fq_script, processor=sys.executable):
    """Run a monitored script. Show run time, output (stdout), as well as errors (stderr)."""
    print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] Running '{fq_script}' ...\n")
    start_time = time.time()
    result = subprocess.run([processor, fq_script], capture_output=True, text=True)
    end_time = time.time()
    print("Output:")
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)
    elapsed = end_time - start_time
    print(f"Ran for {elapsed:.2f} seconds.")


def main(fq_filename=None, sleep_time=None, processor=sys.executable):
    ''' The main console interface. Scipt file must exist. Time defaults to 3 seconds.
    Paramaters override argurment parsing.'''
    if not processor:
        processor = sys.executable
    if not sleep_time:
        sleep_time = 3
    if not fq_filename:
        parser = argparse.ArgumentParser(
            description="Run a script whenever it is updated."
        )
        parser.add_argument(
            "-i", "--interval",
            type=int,
            default=3,
            help="Seconds between checks (default is 3.)"
        )
        parser.add_argument(
            '-p', "--processor",
            default=sys.executable,
            help="Path to a script file to monitor."
        )
        parser.add_argument(
            "script",
            help="Path to a script file to monitor."
        )

        args = parser.parse_args()
        fq_filename = args.script
        sleep_time = args.interval
        processor = args.processor
    
    if not os.path.isfile(fq_filename):
        print(f"Error: File '{fq_filename}' not found.")
        sys.exit(1)

    last_mtime = os.path.getmtime(fq_filename)
    print(f"Monitoring '{fq_filename}' for changes every {sleep_time} seconds.\nPress Ctrl+C to stop.")
    basename = os.path.basename(fq_filename)

    try:
        while True:
            time.sleep(sleep_time)
            try:
                zmtime = os.path.getmtime(fq_filename)
                if zmtime != last_mtime:
                    print(f"\nChange detected on '{basename}' ... ")
                    run_script(fq_filename, processor)
                    last_mtime = zmtime
            except FileNotFoundError:
                print(f"File '{fq_filename}' was deleted or moved. Waiting for it to reappear...")
                while not os.path.isfile(fq_filename):
                    time.sleep(sleep_time)
                print(f"File '{basename}' is back!")
                last_mtime = os.path.getmtime(fq_filename)
    except KeyboardInterrupt:
        print(f"\nStopped monitoring '{fq_filename}'.")
        sys.exit(1) # observed


if __name__ == "__main__":
    main()
