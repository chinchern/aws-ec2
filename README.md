# Deploy a Streamlit App on AWS EC2

Follow these steps to deploy your Streamlit app on an AWS EC2 instance.

## 🛠️ Step 1: Launch an EC2 Instance

1. Go to the [AWS Console](https://aws.amazon.com/console/) and open the EC2 Service.
2. Click **Launch Instance**.
3. Choose an **Amazon Machine Image (AMI)**:
   - Select **Ubuntu 22.04 LTS** (recommended) or **Amazon Linux**.
4. Choose an **instance type**:
   - **t2.micro** (free tier) is sufficient for testing.
5. Configure the **security group** (Important!):
   - Add **HTTP (port 80)** to allow users to access your app.
   - Add **Custom TCP (port 8501)** for Streamlit.
   - Add **SSH (port 22)** to connect to the server.
6. Launch the instance and download the `.pem` key for SSH access.

---

## 🛠️ Step 2: Connect to Your EC2 Instance

1. Open your terminal and connect to your EC2 instance using SSH:

    ```sh
    ssh -i your-key.pem ubuntu@your-ec2-public-ip
    ```
   or the following for my case:
    ```sh
   ssh -i ~/ssh/ec2-key.pem ec2-user@3.8.143.49
    ```

2. Once connected, update the system:

    ```sh
    sudo apt update && sudo apt upgrade -y
    ```

---

## 🛠️ Step 3: Install Python and Streamlit

1. Install Python and pip:

    ```sh
    sudo apt install python3 python3-pip -y
    ```

2. Install Streamlit:

    ```sh
    pip3 install streamlit
    ```

3. Verify the installation:

    ```sh
    streamlit --version
    ```

---

## 🛠️ Step 4: Upload Your Streamlit App to EC2

### Option 1: Upload the app using SCP (Secure Copy Protocol)

From your local machine, run:

```sh
scp -i your-key.pem your_streamlit_app.py ubuntu@your-ec2-public-ip:~
```
or the following for my case:
```sh
scp -i ~/ssh/ec2-key.pem /Users/lowchinchern/source/aws-ec2/app.py ec2-user@3.8.143.49:~

```

## 🛠️ Step 5: Run Streamlit

1. Run the app with the following command:

    ```sh
    streamlit run app.py --server.port 8501 --server.address 0.0.0.0
    ```

   The `server.address=0.0.0.0` ensures it’s accessible from the internet.


---

## 🛠️ Step 6: Access Your Streamlit App

Open your browser and go to:


You should now see your Streamlit app running! 🎉

---

## 🛠️ Step 7: Keep the App Running (Optional)

If you close the terminal, the app will stop. To keep it running in the background:

```sh
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > output.log 2>&1 &
```

# Understanding Ports in Networking

A **port** is a logical endpoint in a computer network where communication between devices or services occurs. It helps direct data to the correct application or service on a device (like a server or computer).

When you send or receive data over the internet, it's not just the **IP address** that matters — the **port number** helps identify which specific service or application on that device should handle the data.

## Example of Ports in Use:

- **HTTP** (used for web browsing) typically uses **port 80**.
- **HTTPS** (secure web browsing) typically uses **port 443**.
- **Streamlit apps** by default often use **port 8501**.
- **SSH** (used to securely connect to servers) uses **port 22**.

## Ports in Networking

Ports are part of the **Transmission Control Protocol (TCP)** and **User Datagram Protocol (UDP)**. They allow multiple services to run on the same device using different port numbers, so the device knows which application the data is meant for.

## How Ports Work:

Think of it like this:
Imagine your computer is a large building. The **IP address** is the street address, and each **port** is a specific room in that building. When someone wants to send data to you (or a service on your computer), they send it to the building (IP address) and to a specific room (port) where the service is running.

## Common Port Numbers:

- **22**: SSH (used for secure shell access)
- **80**: HTTP (used for regular web traffic)
- **443**: HTTPS (used for secure web traffic)
- **8501**: Streamlit (default port for Streamlit apps)

---

## Example: Ports in AWS EC2 with Streamlit

In your case, when you set up **Streamlit** on an **AWS EC2** instance, you're opening **port 8501** to allow users to access the Streamlit app via the web.




