import torch
from fastai.vision.all import *
import cv2
def model_line():
    

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model= torch.load("C:\\Users\\oozer\\Desktop\\Lane detection\\fastai_model.pth",  map_location=device)

    
    img = cv2.imread(str(get_image_files('C:\\Users\\oozer\\Desktop\\Lane detection\\test_video')[0]))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    def get_pred_for_mobilenet(model, img_array):
        with torch.no_grad():
            image_tensor = img_array.transpose(2,0,1).astype('float32')/255
            x_tensor = torch.from_numpy(image_tensor).unsqueeze(0)
            model_output = F.softmax( model.forward(x_tensor), dim=1 ).cpu().numpy()
        return model_output
    model.eval()
    import copy
    back, left, right = get_pred_for_mobilenet(model,img)[0]
    def ld_detection_overlay(image, left_mask, right_mask):
        res = copy.copy(image)
        res[left_mask > 0.3, :] = [0,0,255]
        res[right_mask > 0.3, :] = [255,0,0]
        return res
    plt.imshow(ld_detection_overlay(img, left, right))
    
    
    plt.imsave('C:\\Users\\oozer\\Desktop\\LAne detection\\pred.png',ld_detection_overlay(img, left, right))
    return 'C:\\Users\\oozer\\Desktop\\LAne detection\\pred.png'