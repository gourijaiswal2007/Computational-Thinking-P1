Computational-Thinking-P1
 
Task 1: Identity Investigation
Objective:
To observe how memory IDs change for different data types when modified.
Action Performed:
A file named `identity_gouri_jaiswal.py` was created. Different data types (integer, string, list, tuple) were modified, and their memory IDs were printed before and after the change using the `id()` function.
 Observation:
- Integer → Memory ID changes after modification  
- String → Memory ID changes after modification  
- Tuple → Memory ID changes after modification  
- List → Memory ID remains the same after modification

Conclusion:
Integer, string, and tuple are immutable data types, meaning they create new memory locations when modified. Lists are mutable, so they modify the same memory location.

Task 2: Nature of Commit History
Action Performed:
A repository was created and a file named `identity_gouri_jaiswal.py` was added. Changes were made to the file based on different data types, and multiple commits were created with messages like "Version 1" and "Version 2".
Question:
Does "Version 2" still exist in the folder?

Answer:
Yes, "Version 2" still exists in the repository. In fact, both Version 1 and Version 2 are present in the commit history. Git does not overwrite previous versions; instead, it stores every version as a separate commit.
Explanation:
Git uses an immutable storage model, which means once a commit is created, it cannot be changed or deleted. Any modification results in the creation of a new commit rather than altering the existing one.

This ensures that:
- The complete history of the project is preserved  
- Previous versions can be accessed at any time  
- Changes can be tracked effectively  
- Data is not lost accidentally  

Conclusion:
Git keeps every version permanently. This proves that commits are immutable, and any change creates a new commit instead of modifying the existing one.

Task 3: Shallow Copy Behavior
Action Performed:
A file named `change.py` was created containing a nested list:
`data = [[10, 20], [30, 40], [50, 60]]`

A copy of the list was created using:
`update_data = list(data)`

An inner element was modified:
`update_data[1][1] = 99`
Both lists were printed.

Observation:
The original list also changed when the copied list was modified.

Explanation:
A shallow copy was created using `list()`. In a shallow copy, only the outer list is copied, but the inner lists still refer to the same memory locations.
Therefore, modifying an inner element in the copied list also affects the original list.

Conclusion:
To avoid this issue, a deep copy should be used, which creates completely independent copies.

Task 4: Commit Immutability
Action Performed:
A file named `data.py` was created and committed with the message "Copied the content from Task1". The commit hash was noted using `git log`.

The commit message was then modified using:
`git commit --amend`

After modification, the new commit hash was recorded.

Observation:
The commit hash changed after modifying the commit message.

Explanation:
A commit hash in Git is generated based on the content, commit message, and metadata. When the commit message was changed, Git created a new commit with a new hash instead of modifying the old one.

Conclusion:
This proves that commits in Git are immutable and cannot be changed once created. Any modification results in a new commit with a different hash.