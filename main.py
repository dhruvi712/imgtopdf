import os
import img2pdf

folder_path=r""

def images_to_pdf(image_folder_path):   

    if os.path.exists(image_folder_path):
        print("Given images folder path verified -- processing")
    else:
        print("Given images folder Not exist ")
        return
    
    images = [imgs for imgs in os.listdir(image_folder_path) if imgs.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    images.sort()

    images_bytes = list()

    for i in images:
        with open(os.path.join(image_folder_path, i), "rb") as im:
            images_bytes.append(im.read())

    pdf_image_bytes = img2pdf.convert(images_bytes)
    with open('Output.pdf', "wb") as pdfFile:
        pdfFile.write(pdf_image_bytes)
        
images_to_pdf(folder_path)
