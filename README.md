# Username-Password Combiner

Combine usernames and passwords from two files into all possible combinations with a colon separator.

## Usage

```bash
python combine_files.py -u usernames.txt -p passwords.txt -o combined_output.txt
```
# Example

Assuming usernames.txt contains
```
["user1", "user2", "user3"]
```
passwords.txt contains
```
["pass1", "pass2", "pass3"]
```
the output in combined_output.txt will be:
```
user1:pass1
user1:pass2
user1:pass3
user2:pass1
user2:pass2
user2:pass3
user3:pass1
user3:pass2
user3:pass3
```

# Requirements
* Python 3.x
* argparse (standard library)
