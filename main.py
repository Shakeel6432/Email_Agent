# from email_sender import send_email
# from email_reader import check_replies
# from llm_agent import generate_reply
# import time

# def main():
#     # User inputs
#     client_email = input("Enter client's email: ")
#     client_name = input("Enter client's name: ")

#     # Send initial email (only once)
#     subject = f"Let's Connect, {client_name}"
#     body = f"Hi {client_name},\n\nI hope this email finds you well. I would love to discuss potential collaboration opportunities.\n\nLooking forward to hearing from you.\n\nBest Regards."
#     send_email(client_email, subject, body)
#     print(f"Initial email has been sent to {client_email}.")

#     # Continuous loop to monitor replies 24/7
#     print("Monitoring for replies...")
#     while True:
#         reply = check_replies(client_email)
#         if reply:
#             print("Reply received!")
#             response = generate_reply(reply)
#             send_email(client_email, "Re: " + subject, response)
#             print("Auto-reply has been sent.")
#         else:
#             print("No reply yet...")

#         time.sleep(120)  # Wait 2 minutes before checking again

# if __name__ == "__main__":
#     main()










from email_sender import send_email
from email_reader import check_replies
from llm_agent import generate_reply
import time
import threading

# A global dictionary to track clients already contacted
client_list = {}

def monitor_replies():
    print("Started background thread to monitor replies...")
    while True:
        for email, name in list(client_list.items()):
            reply = check_replies(email)
            if reply:
                print(f"Reply received from {email}!")
                response = generate_reply(reply)
                send_email(email, f"Re: Let's Connect, {name}", response)
                print(f"Auto-reply sent to {email}")
            else:
                print(f"No reply yet from {email}...")
        time.sleep(120)

def main():
    # Start reply monitoring in the background
    threading.Thread(target=monitor_replies, daemon=True).start()

    # Main loop to send emails to new clients
    while True:
        print("\n--- New Client Email Sender ---")
        client_email = input("Enter client's email (or type 'exit' to quit): ").strip()
        if client_email.lower() == 'exit':
            print("Exiting program...")
            break
        client_name = input("Enter client's name: ").strip()

        # Save to tracking dictionary
        client_list[client_email] = client_name

        # Send initial email
        subject = f"Let's Connect, {client_name}"
        body = f"Hi {client_name},\n\nI hope this email finds you well. I would love to discuss potential collaboration opportunities.\n\nLooking forward to hearing from you.\n\nBest Regards."
        send_email(client_email, subject, body)
        print(f"Initial email has been sent to {client_email}.")

if __name__ == "__main__":
    main()
