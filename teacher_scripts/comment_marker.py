import csv
import pandas as pd
import argparse
import logging
import re

# Map verbosity levels to logging levels
log_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}



# Log messages
logger = logging.getLogger(__name__)


def capitalize_after_period(text):
    # Function to capitalize the first letter after a period
    def capitalize_match(match):
        return match.group(1) + match.group(2).upper()

    # Regular expression to find periods followed by a space and a lowercase letter
    pattern = re.compile(r'(\. |\.\.\. )([a-z])')

    # Replace matches using the capitalize_match function
    corrected_text = pattern.sub(capitalize_match, text)

    return corrected_text
def main():
    logger.info("Input columns must be: [first_name ,last_name ,gender ,class, mark]")
    parser = argparse.ArgumentParser(description="Pass in a csv of student scores and the output will be the comments.")
    parser.add_argument("-i", "--input_filepath", type=str, help="Path to the input student scores - csv_file")
    parser.add_argument("-o", "--output_filepath", default='~/Downloads/students_parsed.csv', type=str, help="Path to the output csv results")
    parser.add_argument('-v', "--verbosity", default='INFO', help="Set the level of the verbosity, DEBUG, INFO")
    args = parser.parse_args()

    # Configure the logger
    logging.basicConfig(
        level=log_levels[args.verbosity.upper()],
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('app.log', 'a')
        ]
    )

    df = pd.read_csv(args.input_filepath)
    df['comment'] = ''
    df_comment_template = pd.read_csv('./comment_template.csv')


    for index, row in df.iterrows():
        print(f"Student {index + 1}:")
        print(f"First Name: {row['first_name']}")
        print(f"Last Name: {row['last_name']}")
        print(f"Gender: {row['gender']}")
        print(f"Class: {row['class']}")
        print(f"SCORE: {row['grade']}\n")

        # Query DataFrame for rows where grade is "C"
        x = df_comment_template.query(f'grade == "{row["grade"]}"')
        random_comment:str = x['comment'].sample(n=1).iloc[0]

        random_comment = random_comment.replace('[NAME]', row['first_name'].strip())

        if row['gender'].upper() == 'M':
            gender = 'he'
            pronoun = 'his'
        elif row['gender'].upper() == 'F':
            gender = 'she'
            pronoun = 'her'
        else:
            raise Exception('column "gender" must be F or M')

        random_comment = random_comment.replace('[GENDER]', gender)
        random_comment = random_comment.replace('[PRONOUN]', pronoun)
        logger.info(capitalize_after_period(random_comment))
        df.at[index, 'comment'] = random_comment

    df.to_csv(args.output_filepath)
    logger.info("Done")

if __name__ == "__main__":
    main()

