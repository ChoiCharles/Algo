class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int lenP = p.length();
        int lenT = t.length();
        int start = 0;
        int end = lenP;
        String part;
        while (end <= lenT) {
            part = t.substring(start, end);
            if (part.compareTo(p) <= 0) {
                answer++;
            }
            start++;
            end++;
        }
        
        return answer;
    }
}