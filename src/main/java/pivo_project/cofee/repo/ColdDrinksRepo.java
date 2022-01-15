package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.ColdDrinks;

public interface ColdDrinksRepo extends JpaRepository<ColdDrinks, Long> {
}
