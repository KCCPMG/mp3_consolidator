from shutil import copyfile
import os
import eyed3


def consolidate_mp3s(input_folders, output_folder):
    track_no = 1
    for folder in input_folders:
        os.chdir(folder)
        print(folder)
        for file in os.listdir():
            print(file)
            output_file = output_folder+'//' + 'Track ' + str(track_no) + '.mp3'
            copyfile(file, output_file)
            audio_file = eyed3.load(output_file)
            audio_file.tag.track_num = track_no
            audio_file.tag.title = 'Track ' + str(track_no)
            audio_file.tag.save()
            track_no += 1
            print(file + ' copied')


def prompt_for_files():
    input_folders = []
    while True:
        answer = input('Enter path of folder to copy, or type "output" to enter the path of the output folder.')
        if answer == "output":
            output_folder = input('Enter the path for your output folder.')
            consolidate_mp3s(input_folders, output_folder)
            break
        else:
            input_folders.append(answer)


prompt_for_files()
