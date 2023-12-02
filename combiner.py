#!/usr/bin/env python3
import argparse

def combine_user_pass(user_file, pass_file, output_file):
    with open(user_file, 'r') as uf, open(pass_file, 'r') as pf, open(output_file, 'w') as of:
        # Read all lines from both files
        usernames = [user.strip() for user in uf.readlines()]
        passwords = [password.strip() for password in pf.readlines()]

        # Combine and write to the output file
        for user in usernames:
            for password in passwords:
                combined_line = f"{user}:{password}\n"
                of.write(combined_line)

    print(f"Combination completed. Results written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Combine usernames and passwords into a single file.')
    parser.add_argument('-u', '--userfile', type=str, required=True, help='Path to the usernames file')
    parser.add_argument('-p', '--passfile', type=str, required=True, help='Path to the passwords file')
    parser.add_argument('-o', '--outputfile', type=str, required=True, help='Path to the output file')

    args = parser.parse_args()

    combine_user_pass(args.userfile, args.passfile, args.outputfile)

if __name__ == "__main__":
    main()
               
