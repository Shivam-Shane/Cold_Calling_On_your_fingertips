def mail_content_handler(recipient_name, company_name, company_work_related):
        """Handles mail body to process like html content"""
        if recipient_name=="":
                recipient_name="Hiring Manager" # default recipient

        body=f"""
                <html>
                    <body>
                        <p>Dear {recipient_name},</p>
                        <p>I hope this email finds you well. My name is Shivam, 
                        and I am an aspiring Machine Learning Engineer with nearly three years of experience in IT, 
                        focusing on developing and deploying scalable machine learning models and workflows. 
                        I came across your organization {company_name} and was impressed by your innovative work in the field 
                        of AI/GEN {company_work_related}. I would love to explore any opportunities where I could contribute my skills in AI and automation.</p>
                        
                        <p>Throughout my career, I have built expertise in Python, TensorFlow, and Scikit-learn, as well as DevOps tools such as Docker and Kubernetes. In my most recent role at Indus Valley Partners, I led the development of a custom monitoring system that automated the categorization of critical service alerts, reducing response times by 77%. I have also worked on machine learning projects, including an AI-powered image caption generator and an automated text summarization tool, demonstrating a track record of delivering impactful solutions.</p>
                        
                        <p>I would be thrilled to discuss how my skills in machine learning, DevOps, and cloud technologies could be valuable to your team. I am attaching my resume for your reference and would appreciate the opportunity to connect further.</p>
                        
                        <p>Thank you for your time and consideration. I look forward to your response.</p>

                        <p>Warm regards,<br/>
                        Shivam<br/>
                        ML Engineer<br/>
                        Phone: +91-98155-44235<br/>
                        Email: <a href="mailto:sk0551460@gmail.com">sk0551460@gmail.com</a><br/>
                        <a href="https://github.com/your-github-profile">GitHub</a> | 
                        <a href="https://www.linkedin.com/in/your-linkedin-profile">LinkedIn</a> | 
                        <a href="https://your-portfolio-site.com">Portfolio</a></p>
                        


                        <p>----------------------------------------------------------------------------------------------<br/>
                        ▽ Switch off as you go | Recycle - Use Less tissues | Print only if necessary<br/>
                        ---------------------------------------------------------------------------------------------------------</p>

                        <p>This document should only be read by those persons to whom it is addressed and is not intended to be relied upon by any person without subsequent written confirmation of its contents. If you have received this email message in error, please destroy it and delete it from your computer. Any form of reproduction, dissemination, copying, disclosure, modification, distribution, and/or publication of this email message is strictly prohibited.</p>
                    </body>
                </html>
                """
        return body