def is_safe_sequence(numbers, skip_one=False):
    if len(numbers) < 2:
        return False
        
    # Try sequence as-is first
    def check_sequence(nums):
        if len(nums) < 2:
            return False
            
        is_increasing = nums[1] > nums[0]
        
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            
            # Check if difference is between 1 and 3
            if abs(diff) < 1 or abs(diff) > 3:
                return False
                
            # Check if sequence maintains direction
            if is_increasing and nums[i] <= nums[i-1]:
                return False
            if not is_increasing and nums[i] >= nums[i-1]:
                return False
                
        return True
    
    # Check original sequence
    if check_sequence(numbers):
        return True
        
    # If allowed to skip one number, try removing each number
    if skip_one:
        for i in range(len(numbers)):
            test_numbers = numbers[:i] + numbers[i+1:]
            if check_sequence(test_numbers):
                return True
                
    return False

safe_count = 0
with open('d2/input.txt', 'r') as file:
    for line in file:
        numbers = [int(x) for x in line.strip().split()]
        if is_safe_sequence(numbers, skip_one=True):
            safe_count += 1
            
print(f"Number of safe sequences: {safe_count}")
