# Add steps/actions here:

terraform init: Run this command to initialize the directory and download the required provider plugins ("local_file")  
terraform plan: Verify what changes Terraform will make to your resources before applying them  
terraform apply: Execute the plan to apply the changes to your infrastructure

## Goal
I need to delete the "2nd" resource without affecting the other resources. The count variable is part of the resource naming convention.

### Here are the Steps to Remove a Single Count-Based Resource in Terraform Without Affecting Others

## Steps

Step 1. **Update the variable to use a list with a null entry**:
   Modify the `variable "files"` block to specify each file individually, replacing the unwanted index with `null`.

   ```hcl
   variable "files" {
     default = [
       "file0.txt",  # index 0
       null,         # index 1
       "file2.txt",  # index 2
       "file3.txt",  # index 3
       "file4.txt"   # index 4
     ]
   }

```hcl
Step 2. #Refactor the resource to use for_each instead of count: Replace the local_file resource block to use for_each with toset(compact(...)) to skip null values.

resource "local_file" "foo" {
  for_each = {
    for idx, filename in var.files : idx => filename
    if filename != null
  }

  content  = "# Some content for file ${each.key}"
  filename = each.value
}

Step 3. #This way, each resource gets a stable key (the original index), but file1.txt (index 1) is omitted.