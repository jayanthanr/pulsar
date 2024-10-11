def main():
    file_name = input("File name: ")
    file_name = file_name.strip()
    file_name = file_name.lower()
    #print(file_name)
    op = check_ext(file_name)
    print(op)

def check_ext(in_str):

    if in_str.endswith(".gif"):
        return "image/gif"
    elif in_str.endswith(".jpg") or in_str.endswith(".jpeg"):
        return "image/jpeg"
    elif in_str.endswith(".png"):
        return "image/png"
    elif in_str.endswith(".pdf"):
        return "application/pdf"
    elif in_str.endswith(".txt"):
        return "text/plain"
    elif in_str.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()
