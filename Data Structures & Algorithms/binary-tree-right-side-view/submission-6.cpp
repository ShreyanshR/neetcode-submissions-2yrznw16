/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        int depth{};
        vector<int> res;

        dfs(depth, res, root);

        return res;
        
    }

    void dfs(int depth, vector<int>& res, TreeNode* root){
        if(!root) return;

        if(depth == res.size()){
            res.push_back(root->val);
        }

        dfs(depth + 1, res, root->right);
        dfs(depth + 1, res, root->left);
    }
};
