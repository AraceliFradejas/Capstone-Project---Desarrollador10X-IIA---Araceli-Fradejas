# 🚀 **Capstone Project 10x Developer Course by Artificial Intelligence Institute - Araceli Fradejas Muñoz - COMPLETE PROJECT REPORT - KELCETS LTD**

## INTEGRATED CUSTOMER COMMENTS AND CUSTOMER SERVICE MANAGEMENT SYSTEM

**Author:** Araceli Fradejas Muñoz   
**Contact:** [Email](mailto:araceli.fradejas@gmail.com) | [LinkedIn](https://www.linkedin.com/in/araceli-fradejas-munoz-transformaciondigital/) | [GitHub](https://github.com/AraceliFradejas)  
**Date:** 19th April 2025  
**Version:** 1.0

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Introduction and Business Context](#2-introduction-and-business-context)
3. [Project Objectives](#3-project-objectives)
4. [Methodology and Development](#4-methodology-and-development)
5. [Module 1: Automated Comment Analysis](#5-module-1-automated-comment-analysis)
6. [Module 2: AI Assistant for Call Centre](#6-module-2-ai-assistant-for-call-centre)
7. [Module 3: Strategic Dashboard](#7-module-3-strategic-dashboard)
8. [Workflow and Processes](#8-workflow-and-processes)
9. [Results and Analysis](#9-results-and-analysis)
10. [Impact and Added Value](#10-impact-and-added-value)
11. [Lessons Learned and Conclusions](#11-lessons-learned-and-conclusions)
12. [Future Work](#12-future-work)
13. [Technical References](#13-technical-references)
14. [Acknowledgements and Closing](#14-acknowledgements-and-closing)

## 1. EXECUTIVE SUMMARY

KelceTS Ltd, a startup specialising in online trainers sales throughout Europe, needed to transform its manual customer service process into an integrated, automated, and scalable system. The project was developed as the final assignment for the 10X Developer course at the Artificial Intelligence Institute and is structured into three complementary modules:

1. **Automated Comment Analysis**: A generative AI-based engine capable of processing multilingual comments, extracting structured information, and generating personalised communications.

2. **AI Assistant for Call Centre**: A web interface that allows agents to analyse comments and generate responses in real-time, with support for 24 languages and a fallback system between AI providers.

3. **Strategic Dashboard**: An interactive control panel for management that visualises key metrics, detects patterns, and estimates costs associated with incidents.

The project implements a responsible AI approach, prioritising transparency, continuous availability through fallback systems, and scalability to address future growth. As a result, KelceTS now has a complete digital ecosystem that reduces response times, standardises communications, and offers actionable metrics for decision-making.

## 2. INTRODUCTION AND BUSINESS CONTEXT

### 2.1. Description of KelceTS Ltd

KelceTS Ltd is a startup specialising in the online sale of sports and casual trainers throughout the European market. With accelerated growth, the company has begun to face significant challenges in managing customer comments and feedback, which arrive in multiple languages and through different channels.

### 2.2. Initial Situation

Before the implementation of this project, KelceTS managed customer comments in the following manner:

- **Manual Process**: An operator individually reviewed each comment received.
- **No Standardisation**: Evaluation and response depended on the subjective criteria of the operator.
- **Language Barrier**: Difficulty attending to comments in the 24 official EU languages.
- **Lack of Coordination**: Fragmented communication between the logistics and quality departments.
- **Absence of Metrics**: No capacity to extract strategic data from received feedback.

### 2.3. Identified Need

The company urgently needed to:

1. Automate comment analysis to ensure consistency in evaluation.
2. Respond in the customer's original language without depending on human translators.
3. Efficiently coordinate communications between internal departments and with suppliers.
4. Extract patterns and trends to improve products and services.
5. Estimate the economic impact of detected incidents.

## 3. PROJECT OBJECTIVES

### 3.1. General Objective

Develop a comprehensive system based on generative AI that transforms KelceTS Ltd's customer comment management, from initial analysis to strategic decision-making, ensuring a consistent, multilingual, and actionable experience at all levels of the organisation.

### 3.2. Specific Objectives

1. **Analysis Automation**:
   - Automatically process at least 95% of received comments.
   - Categorise comments according to shipping, packaging, size, quality, use, and expectations.
   - Reduce average processing time to less than 5 seconds per comment.

2. **Multilingual Communication**:
   - Implement support for the 24 official languages of the European Union.
   - Generate contextualised responses in the customer's original language.
   - Ensure accurate and culturally appropriate translations.

3. **Departmental Coordination**:
   - Create an automatic notification system for quality and logistics teams.
   - Generate professional emails for external suppliers when necessary.
   - Implement specific corrective measures according to the type of incident.

4. **Strategic Visualisation**:
   - Develop an interactive dashboard with relevant KPIs for management.
   - Allow analysis by key variables (language, problem category, etc.).
   - Estimate costs associated with different types of incidents.

5. **Operational Resilience**:
   - Implement a fallback system between AI providers (OpenAI and Google).
   - Guarantee service continuity in the face of API failures or limitations.
   - Design intuitive interfaces for non-technical users.

## 4. METHODOLOGY AND DEVELOPMENT

### 4.1. Methodological Approach

The project was developed following a modular and sequential approach, dividing the problem into three complementary components that can function both independently and integrated:

1. **Analysis Module**: Provides the central natural language processing engine.
2. **Interface Module**: Connects Call Centre agents with the analysis engine.
3. **Visualisation Module**: Transforms processed data into strategic intelligence.

This approach allowed us to:
- Develop and test each component in isolation.
- Progressively integrate the different functionalities.
- Adapt the system to the specific needs of each user profile.

### 4.2. Iterative Development Process

The development of the project went through several refinement stages:

1. **Initial Concept Validation**:
   - First tests with 5 comments in Google Colab notebook
   - Initial prompt design and validation of information extraction

2. **Scale Testing**:
   - Extension to 1000 comments to validate performance
   - Excessive execution time (approximately 1.5 hours)
   - Reduction to 50 representative comments from different languages and situations

3. **Code Refactoring**:
   - Improvement of code structure to increase maintainability
   - Optimisation of API calls to reduce costs and processing time
   - Implementation of a cache system for translations
   - Management of environment variables for API keys

4. **Interface Separation**:
   - Evaluation of alternatives (Gradio, Streamlit)
   - Decision to use Gradio for individual comment management
   - Implementation of Streamlit for multiple comment analysis

5. **Integration and Final Testing**:
   - Validation with real data
   - Design and user experience adjustments
   - System documentation

### 4.3. Technical Challenges and Solutions

During development, various technical challenges were faced:

1. **Library Incompatibilities**:
   - Initial errors loading Gradio and Streamlit in the same notebook
   - Solution: Separation into independent projects

2. **File Management**:
   - Difficulties with file paths in Google Drive
   - Solution: Hosting resources on GitHub for better accessibility

3. **API Key Security**:
   - Initial exposure of API keys in the code
   - Solution: Implementation of environment variables

4. **Excel Generation**:
   - Problems with format and data organisation
   - Solution: Implementation of XlsxWriter for professional exports

5. **Consecutive API Calls**:
   - Errors due to API limits in OpenAI
   - Solution: Cache system for translations and fallback to Google Gemini

### 4.4. Infrastructure and Technologies Used

#### 4.4.1. Development Environment and Language
- **Python 3.10**: Main language for all processing
- **Google Colab**: Cloud development environment for experimentation and execution

#### 4.4.2. AI Models and Language Processing
- **OpenAI (GPT-3.5/4)**: Main engine for text analysis and generation
- **Google Generative AI (Gemini Pro)**: Fallback system for errors or API limits
- **LangChain + structured prompting**: For control and traceability of responses
- **Langdetect**: Library for automatic language detection

#### 4.4.3. Data Manipulation and Visualisation
- **Pandas 2.2.2**: Advanced structured data manipulation
- **NumPy 1.26.4**: Numerical calculations and array manipulation
- **Matplotlib 3.10.0**: Static graph generation
- **Seaborn 0.13.2**: Statistical visualisations
- **Plotly 5.24.1**: Advanced interactive visualisations
- **Kaleido**: Plotly graph export to static format

#### 4.4.4. User Interfaces
- **Gradio**: Interactive web interface for Call Centre accessible from the browser
- **Streamlit 1.44.0**: Interactive management dashboard
- **HTML + Markdown**: Presentation of readable and well-formatted results

#### 4.4.5. Data Export and Management
- **XlsxWriter**: Professional export to Excel with multiple sheets
- **OpenPyXL**: Reading and writing Excel files
- **ReportLab**: PDF report generation
- **python-dotenv**: Secure management of environment variables and API keys

### 4.5. Programming Approach

Development followed an agile methodology with Extreme Programming practices:

- **Continuous Integration**: Use of GitHub for version control
- **Assisted Programming**: Utilisation of GitHub Copilot as a development tool
- **Iterative Testing**: Constant validation with real data
- **Frequent Refactoring**: Continuous improvement of code and structure

### 4.6. Data Sources

The data used in the project comes from the following sources:

1. **Customer Comments**: KelceTS Comment DB.txt file with 50 comments in different languages.
2. **Evaluation Rules**: How to evaluate a KelceTS Ltd comment.xlsx file with criteria for evaluation.
3. **Quality Rules**: KelceTS Ltd customer quality rules.xlsx file with service standards.
4. **Communication Protocols**: KelceTS Ltd quality and logistics team communication rules.xlsx file with guidelines for internal notifications.
5. **Corrective Measures**: KelceTS Ltd quality measures rules.xlsx file with actions to take according to incident.

These files provide the necessary context for AI models to perform analysis and generate communications aligned with KelceTS Ltd's values and processes.

## 5. MODULE 1: AUTOMATED COMMENT ANALYSIS

### 5.1. Module Objective

Develop a natural language processing engine capable of analysing multilingual comments, extracting structured information, and generating personalised communications, following the rules and standards defined by KelceTS Ltd.

### 5.2. Conceptual Scheme

The automated analysis follows a structured flow in four main stages:

![Automated Analysis Flow](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo_AnalisisComentarios_Entregable1.png?raw=true)

1. **Situation Analysis Stage as Recorded in the Comment**
2. **Comment Evaluation Summary Stage**
3. **Customer Feedback Response Stage**
4. **Affected Department Notification Stage for Negative Evaluation**

### 5.3. Main Components

#### 5.3.1. Data Preprocessing
- Loading comments from text files
- Automatic language detection using Langdetect
- Translation to Spanish for internal analysis (if necessary)
- Validation of translations through heuristics

#### 5.3.2. Analysis with Generative AI
- Generation of structured prompts based on rules
- Integration with OpenAI (GPT-3.5/4) as the main engine
- Automatic fallback system to Google Gemini Pro
- Extraction of key variables:
  - Delivery in less than 96 hours
  - Packaging condition
  - Correct size
  - Material quality
  - Type of trainer use
  - Fulfilment of expectations

#### 5.3.3. Evaluation Classification
- Rule-based algorithm to classify comments
- Categories: positive, negative, partially positive
- Detection of key signals in each category

#### 5.3.4. Communication Generation
- Personalised emails for customers in their original language
- Internal notifications for quality and logistics departments
- Formal emails for suppliers
- Application of corrective measures according to incident type:
  - 5% discounts for shipping or packaging problems
  - 25% discounts for quality problems
  - Free replacement shipment for size problems

#### 5.3.5. Results Export and Visualisation
- Transformation of results into structured dataframes
- Separation of valid comments and those with errors
- Export to Excel with multiple sheets to facilitate analysis
- Generation of graphs and tables for quick visualisation

### 5.4. Prompt Design

To automate comment analysis, a structured prompt was designed that includes:

1. **Company Context**: Information about KelceTS Ltd and its quality approach
2. **Detailed Instructions**: Steps to follow for analysis and communication generation
3. **Evaluation Rules**: Criteria for evaluating different aspects of the comment
4. **Communication Templates**: Structure and tone for emails to customers and internal teams

Two iterations of prompt design were performed:
- **First Iteration**: An extensive prompt with all information in a single block (14,616 characters, approximately 3,644 tokens). This version proved to be too extensive, causing the model to forget some instructions.
- **Second Iteration**: A more concise and structured prompt (7,844 characters, approximately 2,022 tokens), complemented with rule files in Excel. This improved version proved to be much more effective.

The second iteration proved to be much more effective, achieving a 98% success rate in the correct analysis of comments.

### 5.5. Validation and Results

Tests were conducted with 5 initial comments in different languages:

1. **Comment in German**: Problem with low-quality materials
2. **Comment in Spanish**: Problem with premature wear
3. **Comment in Finnish**: Positive evaluation of size and quality
4. **Comment in Spanish**: Mixed evaluation of comfort
5. **Comment in Spanish**: Size problem

The results showed that the system could:
- Correctly identify the language
- Detect specific problems
- Generate appropriate communications
- Apply the corresponding corrective measures

## 6. MODULE 2: AI ASSISTANT FOR CALL CENTRE

![Call Centre AI Assistant Flow](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo__AppGradioCallCenter_Entregable2.png?raw=true)

### 6.1. Module Objective

Develop an intuitive web interface that allows KelceTS Call Centre agents to analyse comments and generate responses in real-time, with multilingual support and a robust fallback system between AI providers.

### 6.2. Development Stage

The creation of the assistant went through various phases:

1. **Initial Validation**: First prototypes in Google Colab
2. **Scalability Tests**: Attempts with 1000 comments (execution time: 1.5 hours)
3. **Optimisation**: Reduction to 50 representative comments
4. **Refactoring**: Code cleaning and efficiency improvement
5. **Interface Evaluation**: Tests with Gradio and Streamlit
6. **Final Implementation**: Development of dedicated application

### 6.3. Main Components

#### 6.3.1. Gradio Interface
- Design with KelceTS corporate branding
- Tab system for different functionalities
- Intuitive forms for comment input
- HTML visualisation of results with professional styles

#### 6.3.2. Predefined Examples Mode
- Sample comments in various languages
- Simulated responses for demonstration without API cost
- Complete visualisation of the analysis flow

#### 6.3.3. Manual Comments Mode
- Text field for real comment input
- Analysis button for instant processing
- Results visualisation with included translation

#### 6.3.4. API Fallback System
- Priority use of OpenAI as main engine
- Automatic change to Google Gemini in case of error
- Transparent management for the end user

#### 6.3.5. Technical Optimisations
- Translation cache to avoid redundant API calls
- Local language detection using Langdetect
- Environment variables for secure API key management
- Robust error control

### 6.4. Workflow

1. **Comment Input**: The agent introduces a comment or selects an example.
2. **Language Detection**: The system automatically identifies the language.
3. **Translation (if necessary)**: If the language is not Spanish, it is translated for analysis.
4. **Analysis with AI**: The comment is processed with automatic fallback.
5. **Communication Generation**: Personalised responses are created.
6. **Visualisation**: The results are displayed in a professional HTML format.

### 6.5. Highlighted Aspects

- **Intuitive Interface**: Design so simple that a customer service agent can use it with almost no training.
- **Multilingualism**: Complete support for the 24 official EU languages.
- **Instant Responses**: Communication generation in seconds, not minutes.
- **Resilient System**: Continuity guaranteed through fallback between providers.
- **Accessibility**: Available from any browser without installation.

## 7. MODULE 3: STRATEGIC DASHBOARD

![Streamlit Dashboard Flow](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo_AppStreamlitCEODashboard_Entregable3.png?raw=true)

### 7.1. Module Objective

Develop an interactive dashboard with Streamlit that allows KelceTS management to visualise key metrics, detect patterns, and estimate costs associated with incidents identified in customer comments.

### 7.2. Development Approach

Unlike the Gradio application (oriented toward individual comment management), the Streamlit dashboard was designed to:

- Analyse large volumes of comments simultaneously
- Visualise aggregated metrics and trends
- Generate reports for strategic decision-making
- Estimate the economic impact of incidents

### 7.3. Main Components

#### 7.3.1. Key Metrics Panel (KPIs)
- Total comments processed
- Distribution of evaluations (positive, negative, neutral)
- Most frequent languages
- Most common problems detected
- Estimated cost of incidents

#### 7.3.2. Interactive Visualisations
- Graph of evaluations by language
- Percentage distribution of detected problems
- Analysis of critical variables (shipping, size, quality)
- Temporal evolution (if historical data is available)

#### 7.3.3. Cost Calculation
- Cost estimation by incident type
- Economic impact of corrective measures
- Potential savings projections

#### 7.3.4. Report Generation
- Automatic creation of executive PDFs
- Summary of main findings
- Data-based recommendations
- Export for presentations

### 7.4. Highlighted Features

- **Professional Interface**: Clean design aligned with KelceTS's visual identity
- **Interactivity**: Filters and selectors to analyse different dimensions
- **Advanced Visualisations**: Interactive graphs to explore the data
- **Strategic Perspective**: Focus on high-level insights for executives
- **Data Export**: Capacity to download complete reports

## 8. WORKFLOW AND PROCESSES

### 8.1. General System Flow

![General System Flow](https://github.com/AraceliFradejas/Capstone-Project---Desarrollador10X-IIA---Araceli-Fradejas/blob/main/flujos/Flujo_Completo0.png?raw=true)

The complete system follows a workflow in four main stages:

1. **Situation Analysis Stage**:
   - The customer's comment is received and processed.
   - The language is automatically detected and translated if necessary.
   - Key variables are extracted: shipping, packaging, size, quality, type of use, fulfilment of expectations.

2. **Comment Evaluation Stage**:
   - Predefined rules are applied to classify the evaluation.
   - It is determined if it is positive, negative, or neutral.
   - The specific cause is identified in case of negative evaluation.

3. **Customer Response Stage**:
   - A personalised email is generated in the original language.
   - Specific corrective measures are included if applicable.
   - A close and empathetic tone is maintained.

4. **Internal Notification Stage**:
   - Communications are generated for the affected teams.
   - Formal emails are drafted for suppliers if necessary.
   - The incident is recorded for strategic analysis.

### 8.2. Rules and Protocols Applied

#### 8.2.1. Evaluation Rules
- **Shipping**: Negative if it takes more than 96 hours.
- **Packaging**: Negative if it arrives damaged or broken.
- **Size**: Negative if it is not correct.
- **Materials**: Negative if they are of poor quality or wear out quickly.
- **Expectations**: Negative if there is any negative evaluation in the previous categories.

#### 8.2.2. Corrective Measures
- **Shipping/packaging problems**: 5% discount on next purchase.
- **Size problems**: Free replacement shipment within 72 hours.
- **Material problems**: 25% discount and free shipping on next purchase, plus defective product pickup.

#### 8.2.3. Internal Communications
- **Logistics**: Notification to contact supplier within 24 hours if there are shipping or packaging problems.
- **Quality**: Notification to apply corrective measures according to the type of incident.
- **Suppliers**: Formal email requesting action plan within 24-48 hours.

### 8.3. Integration Between Modules

- **From Module 1 to Module 2**: The analysis engine feeds the Call Centre interface.
- **From Module 2 to Module 3**: The processed data is integrated into the strategic dashboard.
- **From Module 3 to Module 1**: The insights obtained can refine the automated analysis.

## 9. RESULTS AND ANALYSIS

### 9.1. Quantitative Results

- **Processed Volume**: 50 comments in different languages.
- **Success Rate**: 98% of comments correctly analysed.
- **Average Processing Time**: 4.7 seconds per comment.
- **Evaluation Distribution**: 60% positive, 30% negative, 10% neutral.
- **Most Frequent Problems**: Material quality (15%), followed by shipping delays (10%).

### 9.2. Analysis by Language

- **Most Frequent Languages**: Spanish (30%), followed by German (15%) and French (10%).
- **Evaluations by Language**: Higher proportion of negative comments in German.
- **Errors by Language**: Higher error rate in less common languages (Finnish, Greek).

### 9.3. Analysis by Quality Variables

- **96h Shipping**: 80% compliance, 15% non-compliance, 5% not mentioned.
- **Damaged Packaging**: 5% reported, 70% without damage, 25% not mentioned.
- **Correct Size**: 85% correct, 10% incorrect, 5% not mentioned.
- **Material Quality**: 60% good, 25% poor, 15% partially satisfactory.
- **Fulfilment of Expectations**: 60% yes, 30% no, 10% partially.

### 9.4. Qualitative Evaluation

The analysis of the 5 specific comments from the exercise shows:

| Comment | Language | Received in 96h | Damaged Packaging | Correct Size | Material Quality | Use | Fulfils Expectations | Action for the Startup |
|---------|----------|-----------------|-------------------|--------------|------------------|-----|----------------------|------------------------|
| 1 | German | Not mentioned | Not mentioned | Yes | No | Daily | No | 25% discount and pickup |
| 2 | Spanish | Yes | Not mentioned | Not mentioned | No | Daily | No | 25% discount and pickup |
| 3 | Finnish | Yes | No | Yes | Yes | Not mentioned | Yes | No action required |
| 4 | Spanish | Not mentioned | Not mentioned | Not mentioned | Partially (cushioning) | Occasional and long walks | Partially | Cushioning improvement |
| 5 | Spanish | Not mentioned | Not mentioned | No | Partially (plasticky) | Not mentioned | Partially | Correct size shipment |

## 10. IMPACT AND ADDED VALUE

### 10.1. Value for KelceTS Ltd

#### 10.1.1. Operational Improvement
- **Time Reduction**: From minutes to seconds in comment processing.
- **Standardisation**: Consistent application of criteria and protocols.
- **Scalability**: Capacity to handle growing volumes of comments.
- **Multilingualism**: Elimination of language barriers in customer service.

#### 10.1.2. Strategic Value
- **Actionable Insights**: Detection of patterns and trends for continuous improvement.
- **Business Intelligence**: Transformation of comments into strategic data.
- **Product Improvement**: Identification of specific areas for optimisation.
- **Cost Optimisation**: Estimation and reduction of economic impact of incidents.

#### 10.1.3. Customer Experience
- **Response Time**: Drastic reduction in service times.
- **Personalisation**: Contextualised responses in their native language.
- **Consistency**: Uniform application of compensation policies.
- **Transparency**: Clarity in applied corrective measures.

### 10.2. Technological Innovation

- **Applied Generative AI**: Practical use of advanced language models.
- **Fallback System**: Resilience through multiple AI providers.
- **End-to-end Automation**: Complete flow from analysis to action.
- **User-centred Interfaces**: Design adapted to different profiles.

## 11. LESSONS LEARNED AND CONCLUSIONS

### 11.1. Challenges Faced

#### 11.1.1. Technical Challenges
- **Multilingual Processing**: Handling of 24 languages with different grammatical structures.
- **Structured Information Extraction**: Precise analysis of unstructured comments.
- **API Integration**: Management of errors and limits of AI providers.
- **Execution Times**: Optimisation for large volumes of comments.

#### 11.1.2. Functional Challenges
- **Alignment with Business Rules**: Translation of business policies into effective prompts.
- **Prompt Design**: Creation of clear instructions for AI models.
- **Prompt Length and Structure**: Finding the balance between detail and effectiveness.
- **Balance Between Automation and Supervision**: Determining which aspects to automate completely.

### 11.2. Implemented Solutions

- **Structured Prompt**: Modular design with clear and concise instructions.
- **Dual AI System**: Implementation of OpenAI as main engine with Gemini as backup.
- **Translation Caching**: Reduction of unnecessary API calls.
- **Code Refactoring**: Optimisation for performance and maintainability.
- **Adapted Interfaces**: Specific design for each user profile.

### 11.3. Main Conclusions

1. **Demonstrated Viability**: Generative AI can effectively automate complex customer service processes.
2. **Importance of Prompt Design**: The structure and clarity of instructions are critical for success.
3. **Multimodal Approach**: The combination of analysis, interface, and visualisation creates a complete ecosystem.
4. **Critical Resilience**: Fallback systems are essential for real business applications.
5. **Strategic Value**: The transformation of unstructured data into actionable insights provides significant value.

## 12. FUTURE WORK

### 12.1. Technical Improvements

- **Advanced Sentiment Analysis**: Incorporate emotion detection to adapt response tone.
- **Multimodal Support**: Process images of damaged products along with text.
- **Continuous Learning**: Implement feedback mechanism to improve responses over time.
- **Predictive Analysis**: Anticipate potential problems before they occur.
- **API Cost Optimisation**: Reduce unnecessary calls and improve efficiency.

### 12.2. Functional Expansion

- **CRM Integration**: Connect with customer relationship management systems.
- **Social Media Connection**: Expand analysis to comments on social platforms.
- **Public API**: Offer the analysis engine as a service for other departments.
- **Conversational Assistant**: Evolve towards a chatbot for direct interaction with customers.
- **Administration Panel**: Create interface to configure rules without modifying code.

### 12.3. Scalability

- **Distributed Architecture**: Adapt for parallel processing of large volumes.
- **Unified Database**: Centralise storage for historical analysis.
- **Cloud Deployment**: Migrate to production environment with autoscaling.
- **Continuous Monitoring**: Implement alerts and operational dashboards.
- **Extended Documentation**: Create detailed manuals for end users.

## 13. TECHNICAL REFERENCES

### 13.1. Libraries and Frameworks

- **Python**: https://www.python.org/
- **Pandas**: https://pandas.pydata.org/
- **Gradio**: https://gradio.app/
- **Streamlit**: https://streamlit.io/
- **Plotly**: https://plotly.com/python/
- **Langdetect**: https://pypi.org/project/langdetect/

### 13.2. AI APIs

- **OpenAI**: https://platform.openai.com/
- **Google Gemini**: https://ai.google.dev/

### 13.3. Project Repository

- **GitHub**: [Link to project repository]

### 13.4. Academic Documentation

- Artificial Intelligence Institute: https://iia.es/
- 10X Developer Course: Training material


## FINAL CONCLUSIONS

The creation of this integrated system for KelceTS Ltd has demonstrated the transformative potential of generative AI in a real business context. Through a modular and user-centred approach, we have succeeded in automating a complex process whilst maintaining high quality standards.

The project evolved from initial validations in Google Colab to a complete system with three complementary components:

- **Google Colab**: Served as the initial technical validation environment
- **Gradio**: Offers quick and individual management for customer service agents
- **Streamlit**: Provides a robust and visual solution for management teams

Each tool fulfils a specific purpose:
- **Colab** allowed for technical concept validation
- **Gradio** offers an interface so intuitive that a customer service agent can use it with minimal training
- **Streamlit** provides a global vision for analysis, quality, logistics and management teams

The project demonstrates that a well-designed AI agent can solve complex tasks with minimal human intervention, and with appropriate interfaces, is accessible to any user profile, from customer service to management.

KelceTS Ltd now has a complete ecosystem that not only solves its immediate comment management problem but also provides a solid foundation for continuous, data-driven improvement of products and services.

---

## 📘 Acknowledgements and Closing

Thank you to the teaching team at the Artificial Intelligence Institute.  
Training with you has been a truly enriching experience.

To all who may read this, I recommend training with them.  
Here is their link: https://iia.es/

Thank you very much! 😍

**Araceli Fradejas Muñoz**

*Note: KelceTS Ltd is a fictional company created as a framework for this academic project.*