# Discord Selfbot for 7W7 Bot Character Claims

This Python script is a Discord selfbot designed to automatically click a button with the label "Claim waifu" (or similar) in a specific channel, or in all channels if no specific channel is provided. This script is specifically tailored to interact with the "7W7" bot. **Use this script responsibly and at your own risk, as selfbots violate Discord's terms of service.** It utilizes the `discord.py-self` library.

## Disclaimer

Using selfbots is against Discord's Terms of Service and may result in your account being banned. Use this script at your own risk.

## How to Use

1.  **Install Required Libraries:**
    ```bash
    pip install discord.py-self
    ```
2.  **Get your Selfbot Token:**
    *   Log into Discord on your browser.
    *   Open the Developer Tools (`F12` or `Ctrl+Shift+I`).
    *   Go to the "Console" tab.
    *   Paste the following code into the console and press Enter:
        ```javascript
        window.webpackChunkdiscord_app.push([
          [Math.random()],
          {},
          req => {
            if (!req.c) return;
            for (const m of Object.keys(req.c)
              .map(x => req.c[x].exports)
              .filter(x => x)) {
              if (m.default && m.default.getToken !== undefined) {
                return copy(m.default.getToken());
              }
              if (m.getToken !== undefined) {
                return copy(m.getToken());
              }
            }
          },
        ]);
        console.log('%cWorked!', 'font-size: 50px');
        console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
        ```
    *   Your Discord token will now be copied to your clipboard.
3.  **Get the Channel ID (Optional):**
   *   Enable Developer Mode in Discord's settings under "Advanced".
   *   Right-click the desired channel and select "Copy ID".
   *   **If you want the script to work in all channels, you can skip this step.**
4.  **Configure the Script:**
    *   Open the `main.py` file.
    *   Replace `"TOKEN"` with your actual selfbot token.
    *   **If you want to target a specific channel,** replace `None` with the actual target `CHANNEL_ID`. **If you want the script to work in all channels, leave it as `None`.**
    *   The 7W7 bot ID is already set in the code to `705910242285715546`
5.  **Run the Script:**
    ```bash
    python main.py
    ```

## How It Works

*   The script logs into Discord as a selfbot, using the `discord.py-self` library.
*   It monitors messages in either the specified channel, or *all channels* if no channel is specified.
*   If a message is received from the specified "7W7" bot (ID: `705910242285715546`) and contains interactive components (buttons), it checks for a button with the label "Claim waifu" (or a similar claim button, depending on the bot's implementation).
*   If the button is found, the script simulates a click.
*   A message will be printed to the console when a button is clicked, along with the channel ID.
