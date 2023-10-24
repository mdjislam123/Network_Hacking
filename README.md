                                                                            What challenges did you face in the project? How did you solve them? 
As we faced challenges, we remained determined in troubleshooting and debugging to ensure our web application worked flawlessly. Together, we conducted thorough testing to identify and resolve any potential problems, making our application more resilient and meeting the expected requirements.

In our quest to develop and host our web application, we encountered a challenge while using Docker. Although Docker provided a robust platform for containerization and deployment, setting up the Apache httpd server within the Docker container proved to be more complex than expected. We faced difficulties configuring the server and establishing smooth communication between the container and the local host. This hindered the seamless execution of our web application on the Apache server within Docker.
Fortunately, the remedy to this challenge came in the form of Flask, a Python web framework. As we delved into Flask's documentation and explored its features, we quickly realized its potential as a user-friendly and efficient hosting solution. Unlike Docker, Flask offered a straightforward approach to building web applications, allowing us to focus on the application's functionality and development rather than complex container configurations.
With Flask, we could easily create routes, define functionalities, and render templates to build the web application. Flask's simplicity and minimalist design provided a breath of fresh air, enabling us to set up the application quickly and effortlessly on our local host.
Flask's built-in development server also allowed us to run and test the application directly without needing external server setups. This convenience streamlined the development process, empowering us to focus on the application's core features and security. By purposely leaving the search box unsanitized, we created an avenue to execute the planned attack on the web application server, mimicking real-world scenarios for vulnerability analysis.
In essence, Flask was the perfect remedy to the Docker challenge, as it facilitated the smooth development and hosting of the web application. Its user-friendly interface and powerful capabilities resolved the Docker complexities and accelerated the overall development process. As a result, Flask became the backbone of our project, enabling us to delve deeper into web application security, all while providing a rich learning experience in web development.

                                                                            What did you learn by doing this project?
Throughout this project, we have gained substantial knowledge and conducted extensive research. From the project's inception, we have maintained ongoing discussions, engaging in regular Zoom meetings and exchanging WhatsApp messages. Our collaboration has been invaluable in successfully strategizing, developing, and implementing the project. While each member was assigned specific tasks within the group, we actively worked together to identify challenges and their solutions. As we embarked on the project, we familiarized ourselves with local web hosting using Apache httpd and explored the Python library Flask.
In this project, we also delved into various aspects of network architecture, understanding the intricacies of data transmission, routing protocols, and network security. As a valuable addition to our learning journey, we also explored the Python library Scapy. Before diving into Scapy, we recognized the importance of having a solid foundation in networking fundamentals. Concepts like protocols, IP addresses, and data flow in networks became essential building blocks for our understanding of Scapy's functionalities.Our proficiency in Python played a crucial role in effectively leveraging Scapy. As Scapy operates as a Python library, familiarity with Python syntax, data structures, and programming techniques proved indispensable in making the most of this powerful tool. With a solid understanding of networking and Python skills, we embarked on a hands-on learning journey with Scapy. Throughout our exploration of Scapy, we also discovered the importance of responsible and ethical usage, especially in the context of network security. By integrating Scapy into our learning arsenal, we gained practical insights into network analysis and cybersecurity. 

Moreover, it emphasized the importance of handling user inputs securely. We've seen first-hand how a seemingly innocent feature (like a search bar) could be manipulated into a potential attack vector by exploiting the improper handling of user-generated inputs.
The project also underlined the significance of thoroughly reviewing and understanding every line of code before deployment. Leaving the application in debug mode may seem harmless, but as demonstrated in this project, it can lead to potentially catastrophic consequences.
This exercise was an invaluable lesson in the importance of robust application security and will certainly inform our development practices moving forward. By creating and exploiting our vulnerability, we have gained a practical understanding of the importance of application security, something that will be beneficial in all our future projects.
