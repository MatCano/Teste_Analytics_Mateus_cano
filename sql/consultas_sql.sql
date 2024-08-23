SELECT Produto, Categoria, SUM(Quantidade * Preço) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;


SELECT Produto, Categoria, SUM(Quantidade * Preço) AS Total_Vendas
FROM vendas
WHERE EXTRACT(MONTH FROM Data) = 6 AND EXTRACT(YEAR FROM Data) = 2024
GROUP BY Produto, Categoria
ORDER BY Total_Vendas ASC;