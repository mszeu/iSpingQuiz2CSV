# iSpring QUIZ file decoder utility by Marco S. Zuppone - msz@msz.eu
# This utility is released under AGPL 3.0 license.
# Please refer to the LICENSE file for more information about licensing
# and to README.md file for more information about the usage of it.
# iSpring is a registered trademark. iSpring Solutions, Inc.


import argparse
import csv
import json
import os
import zipfile
from pathlib import Path

VERSION = "0.1.0"


def extract_quiz_to_csv(json_file, csv_file):
    # Load the JSON data
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading JSON: {e}")
        return

    questions = []
    # Locate question groups under slides ('sl' -> 'g')
    groups = data.get('sl', {}).get('g', [])
    for group in groups:
        qlist = group.get('S', [])
        for q in qlist:
            try:
                qtype = q.get('tp', 'Unknown')
                # Extract question text from the nested 'D' structure
                question_text = ""
                D = q.get('D', {})
                for para in D.get('d', []):
                    for segment in para.get('c', []):
                        question_text += segment.get('t', '')
                # Extract choices and determine correct answer(s)
                choices = []
                correct_answers = []
                C = q.get('C', {})
                for ch in C.get('chs', []):
                    # Each choice text may also be nested
                    choice_text = ""
                    for para in ch.get('t', {}).get('d', []):
                        for segment in para.get('c', []):
                            choice_text += segment.get('t', '')
                    choices.append(choice_text)
                    if ch.get('c'):
                        correct_answers.append(choice_text)

                # Any feedback could be extracted here if present in JSON
                feedback = ""  # Not present in this JSON structure
            except Exception as e:
                print(f"Warning: skipped a question due to error: {e}")
                continue

            questions.append({
                'question': question_text,
                'type': qtype,
                'choices': choices,
                'correct': correct_answers,
                'feedback': feedback
            })

    # Write the results to a CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as out:
        writer = csv.writer(out)
        # Write header
        writer.writerow(['Question', 'Type', 'Choices', 'Correct', 'Feedback'])
        for q in questions:
            # Join choices and correct answers with semicolons for CSV
            choices_str = "; ".join(q['choices'])
            correct_str = "; ".join(q['correct'])
            writer.writerow([q['question'], q['type'], choices_str, correct_str, q['feedback']])


def normalize_csv(csv_file):
    # Experimental, partial implementation. To be Completed.
    max_commas_num = 0
    with open(csv_file, 'r', encoding='utf-8') as f:
        for lines in f:
            print(lines)
            commas_in_line = lines.count(",")
            if commas_in_line > max_commas_num:
                max_commas_num = commas_in_line
    print(max_commas_num)


print("iSpring QUIZ file decoder, version " + VERSION + ", by Marco S. Zuppone - msz@msz.eu - https://msz.eu")
print("To get more info about the usage invoke it with the -h option")
print("This software is open source and it is under the Affero AGPL 3.0 license")
print("")
parser = argparse.ArgumentParser(
    description="Extracts from the iSpring QUIZ file the questions and saves them in a CSV file",
    epilog="For any questions, feedback, suggestions  you can contact the author at msz@msz.eu")
parser.add_argument("quizfile", help="iSpring quiz file")
parser.add_argument("csvfile", nargs="?",help="CSV output file", default=None)
args = parser.parse_args()
if zipfile.is_zipfile(args.quizfile):
    with zipfile.ZipFile(args.quizfile, mode="r") as archive:
        archive.extract("document.json")
        archive.close()
    csv_file_name = ""
    if args.csvfile is None:
        csv_file_name = Path(args.quizfile).stem + ".csv"
    else:
        csv_file_name = args.csvfile
    extract_quiz_to_csv("document.json", csv_file_name)
    os.unlink("document.json")
    # normalize_csv(args.csvfile)
    #test
else:
    print("The file " + args.quizfile + " is not a valid iSpring QUIZ file")
