class Solution {
    public String solution(String code) {
        boolean mode = false;
        String ret = "";
        String[] codeArray = code.split("");
        for (int i = 0; i < codeArray.length; i++) {
            if (codeArray[i].equals("1")) {
                mode = !mode;
            } else {
                if (mode) {
                    if (i % 2 == 1) {
                        ret += codeArray[i];
                    }
                } else {
                    if (i % 2 == 0) {
                        ret += codeArray[i];
                    }
                }
            }
        }
        if (ret.equals("")) {
            ret = "EMPTY";
        }
        return ret;
    }
}