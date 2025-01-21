class Rule:
    id = "102"
    description = "Verify references"
    severity = "HIGH"

    @classmethod
    def match(cls, data):
        results = []
        reservations = []
        try:
            for pool in data["catalyst_center"]["network_settings"]["ip_pools"]:
                for reservation in pool.get("ip_pools_reservations", []):
                    reservations.append(reservation["name"])
                    
            for site in data["catalyst_center"]["sites"]["areas"]:
                for r in site.get("ip_pools_reservations", []):
                    if r not in reservations:
                        results.append("catalyst_center.sites.areas.ip_pools_reservations: {} - {}".format(r, site["name"]))

            for site in data["catalyst_center"]["sites"]["buildings"]:
                for r in site.get("ip_pools_reservations", []):
                    if r not in reservations:
                        results.append("catalyst_center.sites.buildings.ip_pools_reservations: {} - {}".format(r, site["name"]))

            for site in data["catalyst_center"]["sites"]["floors"]:
                for r in site.get("ip_pools_reservations", []):
                    if r not in reservations:
                        results.append("catalyst_center.sites.floors.ip_pools_reservations: {} - {}".format(r, site["name"]))

        except KeyError:
            pass
        return results