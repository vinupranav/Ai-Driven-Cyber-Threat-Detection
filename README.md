### AI Driven Cyber Security Threat Detection
![Cyber Security](https://media.licdn.com/dms/image/C5612AQFIAutNILcKpQ/article-cover_image-shrink_720_1280/0/1603263308267?e=1728518400&v=beta&t=S-cyyDxL_Ge8xbzJnzXM97Nv0tlnd3IVsstss6BcsaQ)


The "Threat Detection in Cyber Security Using AI" project is designed to enhance cybersecurity by developing an intelligent system capable of identifying and responding to potential threats using machine learning algorithms. The project is structured into four distinct steps, each contributing to the overall objective of creating a robust and effective threat detection mechanism. Below is an overview of each step in the project:

Step 1: Data Preprocessing
In the first step, data preprocessing is performed to prepare the dataset for subsequent analysis and machine learning. The project utilizes the CIC-IDS2017 dataset, a well-known dataset in the cybersecurity field, which is stored in a "CSVs" folder within the project directory. This dataset includes a wide range of network traffic data, essential for training the machine learning models. The preprocessing involves cleaning the data, handling missing values, normalizing features, and formatting the dataset to ensure that it is ready for further processing.

Step 2: Attack Data Filtering
The second step involves filtering the data to isolate and analyze specific types of cyber attacks. Using the "all_data.csv" file generated in the previous step, the program creates separate files for each of the 12 attack types contained within the dataset. These files are stored in the "./attacks/" directory. By separating the data into attack-specific files, the project facilitates a more focused and detailed examination of each attack type, which is crucial for effective threat detection.

Step 3: Feature Selection and Machine Learning
In the third step, feature selection is performed on the attack-specific files. The goal here is to identify the most significant features that contribute to the detection of each attack type. The program selects the top four features with the highest weights for each attack file. These selected features are then used as inputs for various machine learning algorithms. Feature selection is a critical step as it ensures that the machine learning models are trained on the most relevant data, improving their accuracy and efficiency.

Step 4: Machine Learning Algorithm Evaluation
In the final step, seven different machine learning algorithms are applied to each attack file to evaluate their effectiveness in detecting cyber threats. Among these algorithms, Naive Bayes achieved the best performance, with an accuracy of around 98%. This high level of accuracy indicates the model's strong capability in correctly identifying various types of attacks within the dataset. The focus on achieving such precise detection makes this system a valuable tool in the fight against cyber threats.
