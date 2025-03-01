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


## 🛠️ Step 5: Run Streamlit

1. Run the app with the following command:

    ```sh
    streamlit run app.py --server.port 8501 --server.address 0.0.0.0
    ```

   The `server.address=0.0.0.0` ensures it’s accessible from the internet.

2. If you encounter an error about `protobuf`, run this command:

    ```sh
    pip install --upgrade protobuf
    ```

---

## 🛠️ Step 6: Access Your Streamlit App

Open your browser and go to:


You should now see your Streamlit app running! 🎉

---

## 🛠️ Step 7: Keep the App Running (Optional)

If you close the terminal, the app will stop. To keep it running in the background:

```sh
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > output.log 2>&1 &
