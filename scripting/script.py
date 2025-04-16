
import json
import sys

def validate_plan(plan_file):
    # Ensure the plan being checked is always printed first
    print(f"Checking plan: {plan_file}")
    try:
        with open(plan_file, 'r') as f:
            plan = json.load(f)
        
        for resource in plan.get("resource_changes", []):
            actions = resource.get("change", {}).get("actions", [])
            resource_address = resource.get("address", "Unknown Resource")
            
            # Check if the action is `destroy`
            if "destroy" in actions:
                return f"Action not allowed: {actions} - Resource {resource_address} is being destroyed. Operation cannot proceed."
            
            # Check if the action is `modify`
            if "modify" in actions:
                before_changes = resource.get("change", {}).get("before", {})
                after_changes = resource.get("change", {}).get("after", {})
                
                # Allow modifications only to `tags` attribute
                if not before_changes.get("tags") or list(before_changes.keys()) != ["tags"]:
                    return f"Action not allowed: {actions} - Invalid modification detected in resource {resource_address}."
                
                # Allow changes only to `GitCommitHash` tag within `tags`
                modified_tags_before = before_changes["tags"]
                modified_tags_after = after_changes.get("tags", {})
                if set(modified_tags_before.keys()) != {"GitCommitHash"} or set(modified_tags_after.keys()) != {"GitCommitHash"}:
                    return f"Action not allowed: {actions} - Tags other than 'GitCommitHash' are being modified in resource {resource_address}."

            elif "create" not in actions:
                return f"Action not allowed: {actions} - Invalid action detected in resource {resource_address}."
        
        return "Plan is valid. Apply can proceed.\n"

    except Exception as e:
        return f"Error processing {plan_file}: {e}\n"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file1.json> <file2.json> ...")
        sys.exit(1)
    
    for plan_file in sys.argv[1:]:
        result = validate_plan(plan_file)
        print(result)