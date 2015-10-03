(def s "catsanddog")
(def dict #{"cat", "cats", "and", "sand", "dog"})
(def s "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab")
(def dict #{"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"})

(defn add-word [w s]
  (str " " w s))

(defn word-break-helper [s dict]
  (if (= s "")
    (list "")
    (apply concat (for [x (range 1 (+ (count s) 1))
                        :when (contains? dict (subs s 0 x))]
                    (map (fn [p] (add-word (subs s 0 x) p))
                         (word (subs s x)
                               dict))))))

(def word (memoize word-break-helper))
(defn word-break [s dict]
  (map (fn [x] (subs x 1)) (word s dict)))
