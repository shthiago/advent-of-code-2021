(ns d3.core
  (:require 
    [clojure.java.io :as io]
    [clojure.string :as str]))

(defn read-file-rows [filename]
    (with-open [r (io/reader filename)] 
        (str/split (slurp r) #"\n\n")))

(defn get-draws [input-first-line]
  (str/split input-first-line #","))

(defn split-board [raw-board]
  ;; Split single raw board into vector of vectors
  (map #(str/split (str/trim %) #" +")
    (str/split raw-board #"\n")))

(defn split-boards [boards]
  ;; Process vector of raw boards into vector of boards in matrix style
  (map split-board boards))

(defn in? 
  ;; True if coll contains elm
  [coll elm]  
  (some #(= elm %) coll))

(defn has-winner-row? [board draws]
  (reduce 
    #(or %1 %2) 
    (map 
      (fn [row] 
        (reduce 
          #(and %1 %2)
          (map 
            #(in? draws %)
            row)))
      board)))

(defn transpose [matrix]
  (apply mapv vector matrix))

(defn has-winner-col? [board draws]
  (has-winner-row? (transpose board) draws))

(defn is-board-winner? [board draws]
  (or (has-winner-row? board draws) (has-winner-col? board draws)))

(defn process-result [board draws]
  (->> 
    board
    (reduce concat)
    (filter #(not (in? draws %)))
    (map #(Integer. %))
    (reduce +)
    (* (Integer. (last draws)))))

(defn solve-first-part [draws boards]
  (loop [k 6
        curr-draws (subvec draws 0 5)]
    (let [winners (filter #(is-board-winner? % curr-draws) boards)]
    (if (> (count winners) 0)
      (println "First board to win:" (process-result (nth winners 0)  curr-draws))
      (recur (inc k) (subvec draws 0 k))))))

(defn draw-until-win [board draws]
  (loop [k 5
        curr-draws (subvec draws 0 k)]
    (if (is-board-winner? board curr-draws)
      curr-draws
      (recur (inc k) (subvec draws 0 k)))))

(defn solve-second-part [draws all-boards]
  (let [boards-that-win (filter #(is-board-winner? % draws) all-boards)]
    (loop [k 5
          curr-draws (subvec draws 0 k)
          boards boards-that-win]
      (let [loosers (filter #(not (is-board-winner? % curr-draws)) boards)]
        (if (= (count loosers) 1)
          (println "Last board to win:" (process-result (nth loosers 0)  (draw-until-win (nth loosers 0) draws)))
          (recur (inc k) (subvec draws 0 k) loosers))))))

(defn -main [& args]
  (let [file_content (read-file-rows "input.txt")
        draws (get-draws (nth file_content 0))
        boards (split-boards (subvec file_content 1))]
    (do 
      (solve-first-part draws boards)
      (solve-second-part draws boards))
    ))

(-main)