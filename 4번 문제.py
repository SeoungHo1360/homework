file_path = "C:\\Users\\deoki\\Downloads\\mbox.txt"

total_matches = 0  
total_revisions = 0 

try:
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('New Revision'):
                revision = int(line.split(': ')[1].strip())
                total_revisions += revision
                total_matches += 1

    if total_matches > 0:
        average = total_revisions / total_matches

        print(f"Total {total_matches} lines are matched")
        print(f"Average : {average:.4f}")
    else:
        print("No lines matched the format 'New Revision' in the file.")

except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류 발생: {str(e)}")