#!/usr/bin/env python3
import os
#solo para invocar otro push
text = os.environ["INPUT_INPUT_TEXT"]
n = os.environ["INPUT_NUM_OF_REPEATS"]
output = text*n
print(f'set-output name=output_text::{output}')