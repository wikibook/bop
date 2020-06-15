import os
import time

# 1. 백업할 파일과 디렉터리는 리스트에 지정됩니다.
# 윈도우에서의 예:
# source = ['"C:\\My Documents"', 'C:\\Code']
# macOS와 리눅스에서의 예:
source = ['/Users/swa/notes']
# 이름에 공백이 포함된 문자열 안에서는 큰따옴표를 써야 합니다.

# 2. 백업 파일은 메인 백업 디렉터리에 저장해야 합니다.
# 윈도우에서의 예:
# target_dir = 'E:\\Backup'
# macOS와 리눅스에서의 예:
target_dir = '/Users/swa/backup'
# 사용할 폴더로 이 값을 변경하는 것을 잊지 마세요.

# 대상 디렉터리가 존재하지 않는 경우 생성합니다
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. 파일은 zip 파일로 백업됩니다.
# 4. 현재 날짜를 메인 디렉터리 내의 하위 디렉터리명으로 사용합니다.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 현재 시간을 zip 파일의 이름으로 사용합니다.
now = time.strftime('%H%M%S')

# 사용자에게서 텍스트를 입력받아 zip 파일의 이름을 만듭니다.
comment = input('Enter a comment --> ')
# 텍스트를 입력했는지 검사합니다.
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# 하위 디렉터리가 존재하지 않으면 생성합니다
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. zip 명령어를 사용해 파일을 zip 파일에 추가합니다
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# 백업 실행
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
