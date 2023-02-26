import subprocess

'''
!python nnunet/predict.py --image_folder data/decathlon/imagesTs \
    --output_folder ~/submit \
    --plan_path data/preprocessed/nnUNetPlansv2.1_plans_3D.pkl \
    --model_paths ~/baseline_model/model.pdparams \
    --postprocessing_json_path ~/baseline_model/postprocessing.json --model_type cascade_lowres \
    --num_threads_preprocessing 1 --num_threads_nifti_save 1 --precision fp16
'''


def infer():
    result = subprocess.run(['python', 'nnunet/predict.py',
                             '--image_folder', 'data/input',
                             '--output_folder', 'data/output',
                             '--plan_path', 'data/preprocessed/nnUNetPlansv2.1_plans_3D.pkl',
                             '--model_paths', 'checkpoints/model.pdparams',
                             '--postprocessing_json_path', 'checkpoints/postprocessing.json',
                             '--num_threads_preprocessing', '1',
                             '--model_type', 'cascade_lowres',
                             '--num_threads_nifti_save', '1',
                             '--precision', 'fp16',
                             ], capture_output=True, text=True)

    print(result.stdout)  # 打印脚本的标准输出
    print(result.stderr)  # 打印脚本的标准错误输出


infer()
