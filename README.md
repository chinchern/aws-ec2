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

# Understanding IP Addresses

An **IP address** (Internet Protocol address) is a unique identifier assigned to each device connected to a computer network that uses the Internet Protocol for communication. It is used to identify and locate devices on the network, allowing them to communicate with each other.

## Two Types of IP Addresses:

### 1. **IPv4 (Internet Protocol version 4):**

- This is the most commonly used version of IP addresses.
- It consists of four sets of numbers (each between 0 and 255) separated by dots.
- Example: `192.168.0.1`

### 2. **IPv6 (Internet Protocol version 6):**

- This is a newer version of IP addresses, designed to replace IPv4 because of the limited number of addresses available in IPv4.
- IPv6 addresses are longer and use hexadecimal (base 16) numbers.
- Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

---

## Purpose of an IP Address:

- **Unique Identification:** Every device on a network (such as a computer, phone, or server) needs a unique IP address to communicate with other devices.
- **Location Addressing:** It serves as the location or address for the device on the internet or local network, similar to how a street address helps identify a house.
- **Routing:** It helps direct data to the correct device. When you send a request (e.g., opening a website), your IP address helps route the response to the correct device.

---

## Types of IP Addresses:

### 1. **Public IP Address:**

- A **public IP address** is used to identify devices on the internet. It is assigned by your Internet Service Provider (ISP).
- Example: `203.0.113.45`

### 2. **Private IP Address:**

- A **private IP address** is used within a local network, such as your home or office. Devices within the same local network can communicate with each other using private IP addresses.
- Example: `192.168.1.1`

---

## How IP Addresses Work:

When you visit a website, for example, your computer or device sends a request to the server hosting the website, using its **IP address**. The server then sends the data (the webpage) back to your device using your **IP address**, ensuring that the data reaches the correct device.

---

## Think of it like this:

An **IP address** is like your **home address** in a city. When someone wants to send you a letter (data), they need your address (IP address) to know where to send it. Similarly, when you're browsing the web, websites need your **IP address** to send information back to your device.



