package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.Product;
import pivo_project.cofee.enumClasses.ProductType;

import java.util.List;

public interface ProductRepo extends JpaRepository<Product, Long> {
    List<Product> findByType(ProductType type);
}
