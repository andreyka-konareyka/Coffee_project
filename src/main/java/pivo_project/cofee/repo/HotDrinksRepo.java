package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.HotDrinks;

public interface HotDrinksRepo extends JpaRepository<HotDrinks, Long> {
}
