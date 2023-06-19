# import React from 'react';
# import {useRef} from 'react';

# // Fix the code​​​​​​‌​‌​​​‌​​‌​‌​​‌‌‌‌‌​‌‌​‌​ below
# function InputWithFocusButton() {
#     const inputRef = useRef(null);
#     return (
#         <div>
#             <input ref={inputRef}/>
#             <button onClick={() => {inputRef.current.focus()}}>Focus input field</button>
#         </div>
#     );
# }

# // Modify this function if you want to change the preview
# // It will not be evaluated as part of the assessment
# export function Preview() {
#     return <InputWithFocusButton />;
# }

# // Do not change
# export default InputWithFocusButton;v

# #
# import math
# def is_duo_digit(number):
#     # Write your code here
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)
#     num = abs(number)
#     first = ''
#     second = ''
#     while num > 0 :
#         digit = num % 10
#         if first == '':
#             first = digit
#         elif second  == '':
#             second = digit
#         elif first != digit and second != digit:
#             return "n"
#         num = math.trunc(num/ 10)
#     return "y"
