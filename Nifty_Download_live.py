import requests
import tkinter as tk
from tkinter import messagebox


def download_csv(index_name, save_path):
    """
    Downloads index data as CSV from NSE and saves it to a file.
    """
    url = (
        "https://www.nseindia.com/api/equity-stockIndices"
        f"?csv=true&index={index_name.replace(' ', '%20').replace('&', '%26')}"
        "&selectValFormat=crores"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/market-data/live-equity-market",
    }

    try:
        with requests.Session() as session:
            # 1) Visit the main page to obtain necessary cookies
            session.get("https://www.nseindia.com/market-data/live-equity-market", headers=headers)

            # 2) Fetch CSV data
            response = session.get(url, headers=headers)
            response.raise_for_status()

            # 3) Save to file
            with open(save_path, "wb") as f:
                f.write(response.content)

        messagebox.showinfo("Success", f"{index_name} data saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download {index_name}\n\n{str(e)}")


# GUI setup
root = tk.Tk()
root.title("📊 NSE Data Downloader")
root.geometry("450x250")
root.configure(bg="#f4f6f9")  # Light gray background

# Title Label
title_label = tk.Label(root, text="📈 NSE Data Downloader",
                       font=("Helvetica", 18, "bold"),
                       bg="#f4f6f9", fg="#2c3e50")
title_label.pack(pady=20)

# Instruction label
sub_label = tk.Label(root, text="Choose an index to download CSV",
                     font=("Arial", 12), bg="#f4f6f9", fg="#34495e")
sub_label.pack(pady=5)


# Styled Button Function
def styled_button(master, text, command, color):
    return tk.Button(master, text=text, font=("Arial", 12, "bold"),
                     bg=color, fg="white", activebackground="#2c3e50",
                     activeforeground="white", relief="flat",
                     padx=20, pady=10, command=command)


# Buttons
btn1 = styled_button(root, "⬇️ Download NIFTY 50",
                     lambda: download_csv("NIFTY 50", "nifty50.csv"), "#27ae60")
btn1.pack(pady=10, ipadx=10)

btn2 = styled_button(root, "⬇️ Download Securities in F&O",
                     lambda: download_csv("SECURITIES IN F&O", "securities_fo.csv"), "#2980b9")
btn2.pack(pady=10, ipadx=10)


# Footer label
footer = tk.Label(root, text="Developed by Rajubhai Prajapati",
                  font=("Arial", 10, "italic"), bg="#f4f6f9", fg="#7f8c8d")
footer.pack(side="bottom", pady=10)


root.mainloop()
