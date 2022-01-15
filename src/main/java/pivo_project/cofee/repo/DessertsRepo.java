package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.Desserts;

public interface DessertsRepo extends JpaRepository<Desserts, Long> {
}

