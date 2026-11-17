class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row[9][9] = {}, col[9][9] = {}, box[9][9] = {};
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                int d = board[i][j] - '1', k = i / 3 * 3 + j / 3;
                if (row[i][d]++ || col[j][d]++ || box[k][d]++) return false;
            }
        return true;
    }
};
