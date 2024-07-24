# Java Exam Automation

This project consists of two main Python scripts, `exam_generator.py` and `exam_grader.py`, designed to automate the creation and grading of Java course exams. Below is an overview of each script and their functionalities.

After cloning this project, you should run the following in order to get all dependencies for your project:

```bash
pip install -r requirements.txt
```

## exam_generator.py

### Overview

The `exam_generator.py` script automates the process of generating and validating Java exam questions, as well as translating them into Spanish. It utilizes `agents` and `crewai` framework to allow large language models for content creation and validation.

### Features

- **Question Generation**: Automatically generates four questions for a Java exam, including both practical and theoretical aspects.
- **Question Validation**: Validates the generated questions against specific criteria, ensuring they cover the desired topics and meet quality standards.
- **Translation**: Translates the validated exam questions into Spanish.

### Environment Setup

Before running the script, ensure the `OPENAI_API_KEY` environment variable is set to your OpenAI API key (if using OpenAI). If you are using local models with Ollama, just set this value to `NA`

### Running the Script

To execute the script, simply run:

```bash
python exam_generator.py
```

## exam_grader.py

### Overview

The `exam_grader.py` script is designed to process and grade Java exam submissions. It reads student answers from an Excel file, grades each response using a language model, and outputs the graded results to a new Excel file.

### Features

- **Data Extraction**: Reads student email and answers from an input Excel file.
- **Automated Grading**: Utilizes a language model to grade each answer based on predefined questions and scoring criteria.
- **Results Output**: Writes the graded results, including student emails and points awarded for each question, to an output Excel file.

### Environment Setup

Before running the script, ensure the `OPENAI_API_KEY` environment variable is set to your OpenAI API key (if using OpenAI). If you are using local models with Ollama, just set this value to `NA`

### Running the Script

To execute the script, simply run:

```bash
python exam_grader.py
```

## Credits

This project was developed by Eduardo Zuñiga. Special thanks to the open-source community for providing the tools and libraries that made this project possible.

[Website](https://eduzsantillan-dev.vercel.app/)
[Linkedin](https://www.linkedin.com/in/eduzuniga/)
