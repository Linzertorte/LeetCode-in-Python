(def s "catsanddog")
(def dict #{"cat", "cats", "and", "sand", "dog"})

(defn add-word [w s]
  (str " " w s))
(defn dfs [i n s dict]
  (if (= i (+ n 1)) '()
      (concat
       (if (contains? dict (subs s 0 i))
         (map (fn [x] (add-word (subs s 0 i) x)) (word-break-helper (subs s i) dict))
         '())
       (dfs (+ i 1) n s dict))))

(defn word-break-helper [s dict]
  (if (= s "") (list "") (dfs 1 (count s) s dict)))

(defn word-break [s dict]
  (map (fn [x] (subs x 1)) (word-break-helper s dict)))
