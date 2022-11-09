/*https://learndb.ru/courses/task/69

Задача
	Найди самые дорогие товары в каждой категории товаров. Выведи столбцы:

	category_name - название категории товара;
	product_name - название товара;
	price - стоимость товара.
	Отсортируй результат сначала по названию категории, затем по названию товара.

	Помни, что в подзапросах тоже можно выполнять соединение таблиц.*/
	
SELECT
    c.name category_name
  , p.name product_name
  , pp.price
FROM   category c
  INNER JOIN product p
    ON c.category_id = p.category_id
  INNER JOIN product_price pp
    ON p.product_id = pp.product_id
WHERE pp.price = (SELECT MAX(tpp.price)
                  FROM category ct
                    INNER JOIN product tp
                      ON ct.category_id = tp.category_id
                  INNER JOIN product_price tpp
                    ON tp.product_id = tpp.product_id
                  WHERE ct.name = c.name)
ORDER BY category_name, product_name