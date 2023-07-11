# Password Generator

A simple password generator program written in Python. This program generates random passwords, hashes them for security, and evaluates their strength.

## Features

- Generates random passwords using a combination of letters, digits, and special characters.
- Hashes the generated password using the SHA-256 algorithm for added security.
- Evaluates the strength of the generated password based on length and provides feedback.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/password-generator.git
   ```
   
2. Change to the project directory:
   ```shell
    cd password-generator
    ```
## Usage

1. Run the main.py script:

    ```shell
    python main.py
    ```
2. Follow the prompts to specify the desired length of the password.

3. The program will generate a random password, hash it, and display the generated password, hashed password, and password strength.

4. Repeat the process to generate new passwords or exit the program.

PS: As this is a small program made solely for the purpose of helping CLI users to quickly have a random strong password and its hash right on time/soon as they need it, without the need to have to turn to a webbroser and use a password generator + hash it on another webpage, this program does not save the hashes nor the passwords to any file, extension or programm (.exe). For that it is advised that the user copy both, generated password and its SHA256 generated hash to a file or password manager of its own choice.  

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

