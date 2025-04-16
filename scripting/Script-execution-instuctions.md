instructions for executing the provided script against the `*.tfplan` test files located in the same directory:
### **Key Notes**
- The script validates each file according to the defined criteria and prints results to the terminal.
---

### **Setup**
1. **Ensure Python is Installed:**
   - Verify that Python 3.x is installed on your system by running this command in the terminal:
     ```bash
     python --version
     ```
  

2. **Place Files in the Same Directory:**
   - Save the script as `script.py` in the directory containing the test files (`tfplan-1.json`, `tfplan-2.json`, `tfplan-3.json`).
   - The directory should now look something like this:
     ```
     /path/to/directory/
       ├── script.py
       ├── tfplan-1.json
       ├── tfplan-2.json
       ├── tfplan-3.json
     ```

---

### **Execution**
1. **Open the Terminal:**
   - On Windows, you can use Command Prompt or PowerShell.
   

2. **Navigate to the Directory:**
   Use the `cd` command to move into the folder containing `script.py` and the test files. For example:
   ```bash
   cd /path/to/directory
   ```

3. **Run the Script:**
   To execute the script for all test files, run the following commands:
   ```bash
   python script.py tfplan-1.json tfplan-2.json tfplan-3.json
   ```



### **Expected Output**
- For valid plans, the script will output:
  ```
  Checking plan: tfplan-1.json
  Plan is valid. Apply can proceed.

  Checking plan: tfplan-2.json
  Plan is valid. Apply can proceed.

  
  ```

- For invalid plans, the script will specify the action that caused the violation:
  ```
  Checking plan: tfplan-3.json
  Action not allowed: ['no-op'] - Invalid action detected in resource module.aihub.azapi_resource.AISearchServices.
  ```



