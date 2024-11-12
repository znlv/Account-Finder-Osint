
---

# Account Finder Project

This Python project allows users to search for social media accounts on various platforms such as Twitter, Facebook, YouTube, and Instagram. The user can provide a username, and the program will check if that username exists on the specified platforms and display the results.

## Features

- **Twitter Account Finder**: Check if a username exists on Twitter.
- **Facebook Account Finder**: Check if a username exists on Facebook.
- **YouTube Account Finder**: Check if a username exists on YouTube.
- **Instagram Account Finder**: Check if a username exists on Instagram.
- **User-friendly Interface**: Choose between different functionalities via a simple menu.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- Required Python libraries:
  - `subprocess`
  - `json`
  - `time`
  
  You can install any missing packages using `pip`.

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project folder:

   ```bash
   cd <project_folder>
   ```

3. Install any necessary dependencies (if you have a `requirements.txt` file):

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure the paths to the API scripts (`x.py`, `fb.py`, `yt.py`) and `config.json` are correctly set in the script. These should contain the necessary API logic and credentials for each platform (Twitter, Facebook, YouTube).

## Usage

1. **Run the Program**:
   You can start the program by running the main Python script:

   ```bash
   python main.py
   ```

2. **Choose an Option**:
   Once the program is running, you will be presented with a menu. Here, you can choose between the following options:

   - `1` - **Account Finder**: Search for social media accounts.
   - `2` - **Twitter Data Finder**: (You can expand on this option later).

3. **Account Finder**:
   If you select option `1`, you will be prompted to enter a username. The program will search across the following platforms:

   - **Twitter**
   - **Facebook**
   - **YouTube**
   - **Instagram**

   It will then display whether an account is found on each platform or not.

4. **Twitter Profile Finder**:
   If you select option `2`, the program currently prints "nigger" as a placeholder. You can expand this function to search for more data related to a Twitter profile.

## Code Structure

### Main Script (main.py)

- **Imports**: Imports necessary libraries (`os`, `subprocess`, `json`, `time`).
- **Logo and UI**: Displays ASCII logos and user choices.
- **Function Definitions**: Functions like `clear()`, `slowprint()`, `check_status_code()`, and platform-specific functions (`twitter()`, `fb()`, `yt()`) that interact with the respective APIs to search for accounts.
- **Main Flow**: The `choicescreen()` function runs the main flow where users select what they want to search for.

### File Structure

```
├── src/
│   ├── apis/                # Contains scripts for interacting with different APIs (x.py, fb.py, yt.py)
│   ├── config/              # Contains the configuration files (config.json)
│   └── func/                # Contains helper functions (e.g., slow.py for slow printing)
└── main.py                   # Main script to run the program
```

### Configuration

The configuration is loaded from `config/config.json`. You need to provide your API tokens and other credentials in this JSON file.

Example `config.json`:

```json
{
    "twitter": {
        "bearer_token": "YOUR_TWITTER_BEARER_TOKEN"
    },
    "facebook": {
        "access_token": "YOUR_FACEBOOK_ACCESS_TOKEN"
    },
    "yt": {
        "api_key": "YOUR_YOUTUBE_API_KEY"
    },
    "instagram": {
        "access_token": "YOUR_INSTAGRAM_ACCESS_TOKEN"
    }
}
```

### Slow Print

The program includes a feature for "slow printing" to display text one character at a time, adding a more engaging effect. The slow print function (`slowprint()`) is handled by the `slow.py` script.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, create a branch for your feature, and submit a pull request. If you have suggestions or bug reports, open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- The placeholder `twitterprofile()` function needs to be expanded to provide actual functionality, such as fetching and displaying specific data from a Twitter profile.
- Make sure you replace the placeholders with actual API calls to interact with the respective platforms (Twitter, Facebook, YouTube, Instagram).
  
