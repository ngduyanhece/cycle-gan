import os

all_input = os.listdir('input')
all_input_path = [os.path.join('input',im) for im in all_input]

# print(all_input_path)

for im in all_input:
    im_path = os.path.join('input',im)
    output_path = os.path.join('output',im)
    command = "python inference.py --model pretrained/pt2hw.pb --input ./{} --output ./{} --image_size 128".format(im_path,output_path)
    print(command)
    os.system(command)