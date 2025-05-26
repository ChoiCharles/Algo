class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        boolean[] isSkipped = new boolean[26];

        for (char c : skip.toCharArray()) {
            isSkipped[c - 'a'] = true;
        }

        for (char c : s.toCharArray()) {
            int count = 0;
            int currentChar = c - 'a';

            while (count < index) {
                currentChar = (currentChar + 1) % 26;
                if (!isSkipped[currentChar]) {
                    count++;
                }
            }

            answer.append((char) (currentChar + 'a'));
        }

        return answer.toString();
    }
}