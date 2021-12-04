(ns d3.core
  (:require 
    [clojure.java.io :as io]
    [clojure.string :as str]))


(defn get-lines [file]
  (with-open [r (io/reader file)]
    (str/split-lines (slurp r))))

(defn str-as-int-vector [input]
  (map #(Character/digit % 10) input))

(defn exp [x n]
  (loop [acc 1 n n]
    (if (zero? n) acc
        (recur (* x acc) (dec n)))))

(defn binvec-to-dec [input]
  (reduce + (map-indexed #(* (exp 2 %1) %2) (reverse input))))

(defn most-common-at [list index]
  (let [thresh (/ (count list) 2) accum (apply map + list)]
    (if (>= (nth accum index) thresh) 1 0)))

(defn least-common-at [list index]
  (let [thresh (/ (count list) 2) accum (apply map + list)]
    (if (>= (nth accum index) thresh) 0 1)))

(defn calc-oxygen-rating [measures]
  (binvec-to-dec (first (loop [list measures index 0]
    (if (= (count list) 1)
      list
      (let [most-common (most-common-at list index)]
        (recur (filter #(= (nth % index) most-common) list) (inc index))))))))

(defn calc-scrubber-rating [measures]
  (binvec-to-dec (first (loop [list measures index 0]
    (if (= (count list) 1)
      list
      (let [least-common (least-common-at list index)]
        (recur (filter #(= (nth % index) least-common) list) (inc index))))))))


(defn -main [& args]
  (def measures (map str-as-int-vector (get-lines "input.txt")))
  (def measures-accum (apply map + measures))

  (def half-measures (/ (count measures) 2))

  (def gamma-rate-vec (map #(if (>= % half-measures) 1 0) measures-accum))
  (def epsilon-rate-vec (map #(if (= % 1) 0 1) gamma-rate-vec))

  (println "Gamma rate bin:" (reduce str gamma-rate-vec))
  (println "Epsilon rate bin:" (reduce str epsilon-rate-vec))

  (let [gamma-rate-dec (binvec-to-dec gamma-rate-vec) 
        epsilon-rate-dec (binvec-to-dec epsilon-rate-vec)]
    (println "Gamma rate:" gamma-rate-dec)
    (println "Epsilon rate:" epsilon-rate-dec)
    (println "P1 result:" (* gamma-rate-dec epsilon-rate-dec)))
    
    
  (let [oxygen-rating (calc-oxygen-rating measures) scrubber-rating (calc-scrubber-rating measures)]
    (println "Oxygen rating:" oxygen-rating)
    (println "CO2 scrubber rating:" scrubber-rating)
    (println "P2 result:" (* oxygen-rating scrubber-rating))))