class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for (int i = 0; i < strs.length; i++){
            int[] temp = new int[26];
            for (int j = 0; j < strs[i].length(); j++){
                temp[strs[i].charAt(j) - 'a']++;
            }
            String key = Arrays.toString(temp);
            if (res.containsKey(key)){
                res.get(key).add(strs[i]);
            }
            else{
                List<String> val = new ArrayList<>();
                val.add(strs[i]);
                res.put(key,val);
            }
        }
        return new ArrayList<>(res.values());
    }
}
