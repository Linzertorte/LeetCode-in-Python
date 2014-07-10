public class Solution {
	private boolean matchFrom(int i, int len, String s, String p) {
		int n = p.length();
		if (i + n > len)
			return false;
		for (int j = 0; j < n; j++)
			if (p.charAt(j) != '?' && p.charAt(j) != s.charAt(i + j))
				return false;
		return true;
	}

	public boolean isMatch(String s, String p) {
		int len = s.length();
		String[] chunks = p.split("\\*+", -1);
		int cnt = chunks.length;
		if (cnt == 1)// no stars
			return s.length() == p.length() && matchFrom(0, len, s, p);
		int l = chunks[0].length();
		int r = chunks[cnt - 1].length();
		if (l + r > len || !matchFrom(0, len, s, chunks[0])
				|| !matchFrom(len - r, len, s, chunks[cnt - 1]))
			return false;
		int begin = l;
		len -= r;
		for (int i = 1; i < cnt - 1; i++) {
			while (begin < len && !matchFrom(begin, len, s, chunks[i]))
				begin++;
			if (begin == len)
				return false;
			begin += chunks[i].length();
		}
		return true;
	}
}
