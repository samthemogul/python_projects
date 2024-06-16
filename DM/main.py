
import argparse
import os
import shutil


def clean_directory(directory, log_window, size_threshold):
        
        dir_path = directory
        
        log_res = []
        for file_path in os.listdir(dir_path):
                original_path = os.path.join(dir_path, file_path)
        # check if current file_path is a file
                if os.path.isfile(original_path):
                        # add filename to list
                        split_tup = os.path.splitext(file_path)
                        file_extension = split_tup[1]
                        if file_extension == ".log":
                                log_res.append(file_path)
                        valid_ext = [".log", ".csv", ".txt"]
                        if not file_extension in valid_ext:
                                print("Unknown extension: ", file_path)
                        else:
                                with open(original_path, mode="r") as f:
                                        size = os.path.getsize(original_path)
                                        new_size = size / 1000
                                def file_size_checker(size_value):
                                        sub_path = os.path.join(dir_path, file_extension[1:], f"large_{file_extension[1:]}_files", file_path )
                                        if size_value > size_threshold:
                                                if os.path.exists(os.path.join(dir_path, file_extension[1:], f"large_{file_extension[1:]}_files")):
                                                        shutil.move(os.path.join(dir_path, file_path), sub_path)
                                                else:
                                                        os.mkdir(os.path.join(dir_path, file_extension[1:], f"large_{file_extension[1:]}_files"))
                                                        shutil.move(os.path.join(dir_path, file_path), sub_path)
                                        else:
                                                shutil.move(os.path.join(dir_path, file_path), os.path.join(dir_path, file_extension[1:], file_path ))
                                if os.path.exists(os.path.join(dir_path, file_extension[1:])):
                                        file_size_checker(new_size)  
                                else:
                                        os.mkdir(os.path.join(dir_path, file_extension[1:]))
                                        file_size_checker(new_size)  

        def log_cleaner(log_list):
                sorted_logs = sorted(log_list)
                latest_logs = sorted_logs[:-(log_window + 1):-1]
                for log_file in os.listdir(os.path.join(dir_path, "log")):
                        if os.path.isfile(os.path.join(dir_path, "log", log_file)):
                                if not log_file in latest_logs:
                                        os.remove(os.path.join(dir_path, "log", log_file))

        log_cleaner(log_res)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean up a messy data directory')
    parser.add_argument('directory', help='the directory to clean')
    parser.add_argument('--log-window',
            dest='log_window',
            default=30, # retain 30 log files by default
            type=int, 
            help='log retention policy: how many most recent log files to keep')
    parser.add_argument('--size-threshold',
            dest='size_threshold',
            default=50, # 50KB default
            type=int, 
            help='file size threshold: how large is a large text file')
    directory = parser.parse_args().directory
    log_window = parser.parse_args().log_window
    size_threshold = parser.parse_args().size_threshold

    clean_directory(directory, log_window, size_threshold)
